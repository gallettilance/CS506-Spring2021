import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.decomposition import PCA
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import StandardScaler, MinMaxScaler, PolynomialFeatures
from sklearn.metrics import mean_squared_error, confusion_matrix

N_COMPONENTS = 200

# Load files into DataFrames
X_train = pd.read_csv("./data/X_train_stemmed.csv")
X_submission = pd.read_csv("./data/X_submission_stemmed.csv")


"""
    In case you want to do more processing without running the
    feature extraction file again (not recommended) - you can
    merge the datasets, do the feature extraction / processing
    then split them again as such:
"""
# df = pd.concat([X_train, X_submission])
#
# stemmed = df['StemmedSummary'].replace("", np.nan).dropna().sample(frac=.015)
# vectorizer = CountVectorizer(stop_words='english', ngram_range=(1,2), max_df=.95, min_df=50).fit(stemmed)
# X_train_vect = vectorizer.transform(df['StemmedSummary'].fillna(""))
# X_train_df = pd.DataFrame(X_train_vect.toarray(), columns=vectorizer.get_feature_names()).set_index(df.index.values)
# df = df.join(X_train_df)
#
# X_train_words = X_train.drop(columns=['Id', 'Text', 'ProductId', 'Score', 'UserId', 'HelpfulnessNumerator', 'HelpfulnessDenominator', 'Time', 'Helpfulness', 'Month', 'Year', 'PoductAvgScore', 'UserAvgScore', 'UserHarshness', 'PoductScoreStd', 'ReviewLength', 'SummaryLength']).fillna(0)
#
# vectorizer = TfidfTransformer().fit(X_train_words)
# X_train_vect = vectorizer.transform(X_train_words)
# X_train = X_train[['Id', 'Text', 'ProductId', 'Score', 'UserId', 'HelpfulnessNumerator', 'HelpfulnessDenominator', 'Time', 'Helpfulness', 'Month', 'Year', 'PoductAvgScore', 'UserAvgScore', 'UserHarshness', 'PoductScoreStd', 'ReviewLength', 'SummaryLength']].join(pd.DataFrame.sparse.from_spmatrix(X_train_vect, columns=X_train_words.columns.tolist()).set_index(X_train.index.values))
#
# df.to_csv("./data/train_stemmed_cv.csv", index=False)
#
# X_submission = df[df['Score'].isnull()]
# X_train = df[df['Score'].notnull()]

print(X_train.head())
print()
print(X_submission.head())

# Split training set into training and testing set
X_train, X_test, Y_train, Y_test = train_test_split(
        X_train.drop(['Score'], axis=1),
        X_train['Score'],
        test_size=1/9.0,
        random_state=0
    )

# Process the DataFrames
# This is where you can do more feature extraction
X_train_processed = X_train.drop(columns=['Id', 'Text', 'ProductId', 'UserId'])
X_test_processed = X_test.drop(columns=['Id', 'Text', 'ProductId', 'UserId'])
X_submission_processed = X_submission.drop(columns=['Id', 'Text', 'ProductId', 'UserId', 'Score'])

# I tried to add some interaction terms - then SVD takes a bit longer
poly = PolynomialFeatures(interaction_only=True, include_bias = False).fit(X_train_processed)
X_train_processed = poly.transform(X_train_processed)
X_test_processed = poly.transform(X_test_processed)
X_submission_processed = poly.transform(X_submission_processed)

# Scales the data to the (0, 1) range
# You can also use StandarScalar
scaler = MinMaxScaler().fit(X_train_processed)
X_train_processed = scaler.transform(X_train_processed)
X_test_processed = scaler.transform(X_test_processed)
X_submission_processed = scaler.transform(X_submission_processed)

# Visualize the singular value plot
# u,s,vt=np.linalg.svd(X_train_processed,full_matrices=False)
# _ = plt.plot(s)
# plt.title('Singular values of X_train')
# # plt.show()

# Pick N_COMPONENTS based on above plot
pca = PCA(n_components=N_COMPONENTS).fit(X_train_processed)
X_train_processed = pca.transform(X_train_processed)
X_test_processed = pca.transform(X_test_processed)
X_submission_processed = pca.transform(X_submission_processed)

# Trying to set class weights manually
class_weight = {1.0: 1.5, 2.0: 3.0, 3.0: 2.5, 4.0: 1.5, 5.0: 0.5}

# Learn the model
# Note: I experimented with a few penalty / solvers
lr = LogisticRegression(penalty='l1', verbose=2, solver='saga', max_iter=300, class_weight=class_weight)

# Boost the model
# Note: it took too much time to run so I didn't use it
# bagging = AdaBoostClassifier(lr, n_estimators=30, n_jobs=3)

model = lr.fit(X_train_processed, Y_train)

# Predict the score using the model
Y_test_predictions = model.predict(X_test_processed)
X_submission['Score'] = model.predict(X_submission_processed)

# Evaluate your model on the testing set
print("RMSE on testing set = ", math.sqrt(mean_squared_error(Y_test, Y_test_predictions)))

# Plot a confusion matrix
cm = confusion_matrix(Y_test, Y_test_predictions, normalize='true')
sns.heatmap(cm, annot=True)
plt.title('Confusion matrix of the classifier')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

# Note: based on the confusion matrix you could
# play around with the weights

# Create the submission file
submission = X_submission[['Id', 'Score']]
submission.to_csv("./data/submission.csv", index=False)
