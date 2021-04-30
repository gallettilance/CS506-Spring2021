import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import matplotlib.pyplot as plt

nltk.download('stopwords')

trainingSet = pd.read_csv("./data/train.csv")
testingSet = pd.read_csv("./data/test.csv")

print("train.csv shape is ", trainingSet.shape)
print("test.csv shape is ", testingSet.shape)

print()

print(trainingSet.head())
print()
print(testingSet.head())

print()

print(trainingSet.describe())

trainingSet['Score'].value_counts().plot(kind='bar', legend=True, alpha=.5)
plt.title("Count of Scores")
plt.show()

trainingSet['ProductId'].value_counts().nlargest(25).plot(kind='bar', legend=True, alpha=.5)
plt.title("Top 25 most rated Products")
plt.show()

trainingSet['ProductId'].value_counts().nsmallest(25).plot(kind='bar', legend=True, alpha=.5)
plt.title("Top 25 least rated Products")
plt.show()

trainingSet['UserId'].value_counts().nlargest(25).plot(kind='bar', legend=True, alpha=.5)
plt.title("Top 25 Reviewers")
plt.show()

trainingSet['UserId'].value_counts().nsmallest(25).plot(kind='bar', legend=True, alpha=.5)
plt.title("Lowest 25 Reviewers")
plt.show()

trainingSet[['Score', 'HelpfulnessNumerator']].groupby('Score').mean().plot(kind='bar', legend=True, alpha=.5)
plt.title("Mean Helpfulness Numerator per Score")
plt.show()

trainingSet[['Score', 'ProductId']].groupby('ProductId').mean().nlargest(25, 'Score').plot(kind='bar', legend=True, alpha=.5)
plt.title("Top 25 best rated Products")
plt.show()

trainingSet[['Score', 'ProductId']].groupby('ProductId').mean().nsmallest(25, 'Score').plot(kind='bar', legend=True, alpha=.5)
plt.title("Top 25 worst rated Products")
plt.show()

trainingSet[['Score', 'UserId']].groupby('UserId').mean().nlargest(25, 'Score').plot(kind='bar', legend=True, alpha=.5)
plt.title("Top 25 kindest Reviewers")
plt.show()

trainingSet[['Score', 'UserId']].groupby('UserId').mean().nsmallest(25, 'Score').plot(kind='bar', legend=True, alpha=.5)
plt.title("Top 25 harshest Reviewers")
plt.show()

trainingSet[trainingSet['ProductId'].isin(trainingSet['ProductId'].value_counts().nlargest(25).index.tolist())][['Score', 'ProductId']].groupby('ProductId').mean().plot(kind='bar', legend=True, alpha=.5)
plt.title("Mean of top 25 most rated Products")
plt.show()

trainingSet[trainingSet['ProductId'].isin(trainingSet['ProductId'].value_counts().nsmallest(25).index.tolist())][['Score', 'ProductId']].groupby('ProductId').mean().plot(kind='bar', legend=True, alpha=.5)
plt.title("Mean of 25 least rated Products")
plt.show()

trainingSet[trainingSet['UserId'].isin(trainingSet['UserId'].value_counts().nlargest(25).index.tolist())][['Score', 'UserId']].groupby('UserId').mean().plot(kind='bar', legend=True, alpha=.5)
plt.title("Mean of top 25 Reviewers")
plt.show()

trainingSet[trainingSet['UserId'].isin(trainingSet['UserId'].value_counts().nsmallest(25).index.tolist())][['Score', 'UserId']].groupby('UserId').mean().plot(kind='bar', legend=True, alpha=.5)
plt.title("Mean of lowest 25 Reviewers")
plt.show()

trainingSet['Date'] = pd.to_datetime(trainingSet['Time'], unit='s')
trainingSet['Month'] = trainingSet['Date'].dt.month
trainingSet['Year'] = trainingSet['Date'].dt.year
trainingSet['Hour'] = trainingSet['Date'].dt.hour

trainingSet[['Score', 'Hour']].groupby('Hour').mean().plot(kind='bar', legend=True, alpha=.5)
plt.title("Mean Score per Hour")
plt.show()

trainingSet[['Score', 'Month']].groupby('Month').mean().plot(kind='bar', legend=True, alpha=.5)
plt.title("Mean Score per Month")
plt.show()

trainingSet[['Score', 'Year']].groupby('Year').mean().plot(kind='bar', legend=True, alpha=.5)
plt.title("Mean Score per Hour")
plt.show()

trainingSet['ReviewLength'] = trainingSet.apply(lambda row : len(row['Text'].split()) if type(row['Text']) == str else 0, axis = 1)
trainingSet['SummaryLength'] = trainingSet.apply(lambda row : len(row['Summary'].split()) if type(row['Summary']) == str else 0, axis = 1)

trainingSet[['Score', 'SummaryLength']].groupby('Score').mean().plot(kind='bar', legend=True, alpha=.5)
plt.title("Mean Summary Length per Score")
plt.show()

trainingSet[['Score', 'ReviewLength']].groupby('Score').mean().plot(kind='bar', legend=True, alpha=.5)
plt.title("Mean Review Length per Score")
plt.show()

colors = ['r', 'b', 'g', 'c', 'm', 'y', 'k', 'darkorange', 'indigo', 'pink', 'grey']
fig, ax = plt.subplots()
reviews = []
for i in range(1, 6):
    score = trainingSet.where(trainingSet['Score'] == float(i))
    reviews.append(score['ReviewLength'].dropna())

plt.hist(reviews, bins=1000, label=list(range(1, 6)))
ax.legend(loc='upper left')
plt.xlim(0, 300)
plt.title("Review Length per Score")
plt.show()

fig, ax = plt.subplots()
reviews = []
for i in range(1, 6):
    score = trainingSet.where(trainingSet['Score'] == float(i))
    reviews.append(score['SummaryLength'].dropna())

plt.hist(reviews, bins=10, label=list(range(1, 6)))
ax.legend(loc='upper left')
plt.title("Summary Length per Score")
plt.show()

topWords = []
for i in range(1,6):
    words = pd.Series(word_tokenize(' '.join(trainingSet.where(trainingSet['Score'] == float(i))['Summary'].dropna()).lower())).value_counts()
    topWordsForScore = words.where(~words.index.isin(stopwords.words()))
    print("Top 100 words for Score = ", i)
    print(topWordsForScore.nlargest(100).index.tolist())
    print()
    topWords.append(topWordsForScore)

for i in range(len(topWords)):
    fig, ax = plt.subplots()
    allExcepti = topWords[:i] + topWords[i+1:]
    flattened = pd.concat(allExcepti)
    topWords[i] = topWords[i].where(~topWords[i].index.isin(flattened.nlargest( ).index.tolist()))
    print("Top 100 words sort of unique to Score = ", i+1)
    print(topWords[i].nlargest(100).index.tolist())
    print()
    topWords[i].nlargest(100).plot(kind='bar', ax=ax)
    plt.title("Top 100 word counts unique to Score = " + str(i+1))
    plt.show()

