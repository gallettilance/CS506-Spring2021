import pandas as pd

trainingSet = pd.read_csv("./data/train.csv")
testingSet = pd.read_csv("./data/test.csv")

X_test = pd.merge(trainingSet, testingSet, left_on='Id', right_on='Id')
print(X_test.columns)

X_test = X_test.drop(columns=['Score_x'])
X_test = X_test.rename(columns={'Score_y': 'Score'})

print(X_test.columns)
X_test.to_csv("./data/X_submission.csv", index=False)

X_train = trainingSet[trainingSet['Score'].notnull()]
print(trainingSet.shape)
print(X_train.shape)
X_train.to_csv("./data/X_train.csv", index=False)
