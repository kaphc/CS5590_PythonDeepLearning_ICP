# import libraries
from sklearn.naive_bayes import GaussianNB
import pandas as pd
from sklearn.model_selection import train_test_split

# load glass data set
glass = pd.read_csv('data/glass.csv')

# select the feature column
x = glass[['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']]

# select the target column
y = glass['Type']

# split the dataset as 70% for training and 30% for testing
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

# print the train and test shape
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

# create a naive bayes model using GaussianNB()
clf = GaussianNB()

# train the model using fit() method
clf.fit(X_train, y_train)

# print the model accuracy
print('Accuracy of Naive Bayes on training set: {:.2f}'.format(clf.score(X_train, y_train)))
print('Accuracy of Naive Bayes on test set: {:.2f}'.format(clf.score(X_test, y_test)))