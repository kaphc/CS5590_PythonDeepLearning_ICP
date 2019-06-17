# import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

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

# Implement SVM method with RBF Kernel using scikit library
svm = SVC(kernel='rbf')

# train the model using fit() method
svm.fit(X_train, y_train)

print('Accuracy of SVM classifier on training set: {:.2f}'.format(svm.score(X_train, y_train)))
print('Accuracy of SVM classifier on test set: {:.2f}'.format(svm.score(X_test, y_test)))