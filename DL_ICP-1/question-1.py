import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Activation

diabetes_dataset = pd.read_csv("diabetes.csv", header=None).values
print(diabetes_dataset)

X_train, X_test, Y_train, Y_test = train_test_split(diabetes_dataset[:, 0:8], diabetes_dataset[:, 8], test_size=0.25,
                                                    random_state=87)
np.random.seed(155)

my_first_nn = Sequential()

my_first_nn.add(Dense(40, input_dim=8, activation='relu'))
my_first_nn.add(Dense(40, input_dim=40, activation='relu'))
my_first_nn.add(Dense(40, input_dim=23, activation='relu'))
my_first_nn.add(Dense(40, input_dim=8, activation='relu'))

my_first_nn.add(Dense(1, input_dim=8, activation='sigmoid'))

my_first_nn.compile(loss='binary_crossentropy', optimizer='adam')

my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100, verbose=0, initial_epoch=0)

print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test, verbose=0))
