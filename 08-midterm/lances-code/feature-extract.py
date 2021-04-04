import swifter
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

from sklearn.metrics import mean_squared_error, confusion_matrix

from vocablist import *

# Load file into DataFrames
train = pd.read_csv("./data/train.csv")

def process(df):
    # This is where you can / should do all your processing

    df['Helpfulness'] = df['HelpfulnessNumerator'] / df['HelpfulnessDenominator']
    df['Helpfulness'] = df['Helpfulness'].fillna(0)
    
    df['Date'] = pd.to_datetime(df['Time'], unit='s')
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year
    df = df.drop(columns=['Date'])

    movie_ratings = df[["ProductId", "Score"]].groupby("ProductId").mean()
    movie_ratings = movie_ratings.rename(columns={'Score': 'PoductAvgScore'})
    df = pd.merge(df, movie_ratings, on='ProductId', how='left')
    df['PoductAvgScore'] = df['PoductAvgScore'].fillna(df['PoductAvgScore'].mean())

    user_ratings = df[["UserId", "Score"]].groupby("UserId").mean()
    user_ratings = user_ratings.rename(columns={'Score': 'UserAvgScore'})
    df = pd.merge(df, user_ratings, on='UserId', how='left')
    df['UserAvgScore'] = df['UserAvgScore'].fillna(df['UserAvgScore'].mean())

    df['UserHarshness'] = df['UserAvgScore'] - df['PoductAvgScore']

    movie_ratings_std = df[["ProductId", "Score"]].groupby("ProductId").std()
    movie_ratings_std = movie_ratings_std.rename(columns={'Score': 'PoductScoreStd'})
    df = pd.merge(df, movie_ratings_std, on='ProductId', how='left')
    df['PoductScoreStd'] = df['PoductScoreStd'].fillna(1)

    df['ReviewLength'] = df.apply(lambda row : len(row['Text'].split()) if type(row['Text']) == str else 0, axis = 1)
    df['SummaryLength'] = df.apply(lambda row : len(row['Summary'].split()) if type(row['Summary']) == str else 0, axis = 1)
    
    df['Summary'] = df['Summary'].fillna("")
    df['Text'] = df['Text'].fillna("")

    # swifter doesn't support parallel runs for text columns
    # but I like the way it tells you the percentage of the
    # dataframe processed as it's applying the function
    df['StemmedReview'] = df['Summary'].swifter.apply(lambda row : row.lower())

    topWords = []
    for i in range(1,6):
        words = pd.Series(word_tokenize(' '.join(df.where(df['Score'] == float(i))['StemmedReview'].dropna()).lower())).value_counts()
        topWordsForScore = words.where(~words.index.isin(stopwords.words()))
        topWords.append(topWordsForScore.nlargest(200))

    vocab = []
    for i in range(len(topWords)):
        fig, ax = plt.subplots()
        allExcepti = topWords[:i] + topWords[i+1:]
        flattened = pd.concat(allExcepti)
        topWords[i] = topWords[i].where(~topWords[i].index.isin(flattened.nlargest(200).index.tolist()))
        vocab += list(set(topWords[i].index.tolist()))

    # Getting the vocab takes a few minutes so we'll save it locally so we don't need to re-compute it
    pd.Series(vocab).to_csv('vocab.csv')
    
    # just use a subset of the data ~1.5%
    stemmed = df['StemmedReview'].replace("", np.nan).dropna().sample(frac=.015)
    vectorizer = CountVectorizer(stop_words='english', vocabulary=vocab, max_df=.8, min_df=20).fit(stemmed)
    X_train_vect = vectorizer.transform(df['StemmedReview'])
    X_train_df = pd.DataFrame(X_train_vect.toarray(), columns=vectorizer.get_feature_names()).set_index(df.index.values)
    df = df.join(X_train_df)
    
    df = df.drop(columns=["StemmedReview"])
    return df

# Process the DataFrame
train_processed = process(train)
trainX =  train_processed[train_processed['Score'].notnull()]
print(trainX.columns)
print(trainX.head())

test = pd.read_csv("./data/test.csv")

testX= pd.merge(train_processed, test, left_on='Id', right_on='Id')
testX = testX.drop(columns=['Score_x'])
testX = testX.rename(columns={'Score_y': 'Score'})
print(testX.columns)
print(testX.head())

testX.to_csv("./data/X_submission_processed.csv", index=False)
trainX.to_csv("./data/X_train_processed.csv", index=False)
