# import libraries
import numpy as np

# add 15 random numbers to the array using np.random.randint() function
random_vector = np.random.randint(1, 21, size=15, dtype='I')

# to print original array
print("Original array:")
print(random_vector)

# after replacing the maximum value by zero
random_vector[random_vector.argmax()] = 0
print("Updated Array:")
print(random_vector)
