from keras.layers import Input, Dense
from keras.models import Model
import matplotlib.pyplot as plt
from keras.callbacks import TensorBoard
from keras.datasets import fashion_mnist
import numpy as np

(x_train, _), (x_test, _) = fashion_mnist.load_data()
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

encoding_dim = 32
input_img = Input(shape=(784,))

encoded = Dense(8 * encoding_dim, activation='relu')(input_img)

encoder_layer = Dense(encoding_dim, activation='relu')(encoded)

decoded_layer = Dense(8 * encoding_dim, activation='relu')(encoder_layer)

decoded = Dense(784, activation='sigmoid')(decoded_layer)
autoencoder = Model(input_img, decoded)
autoencoder.summary()
autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')

tensorboard = TensorBoard(log_dir='./autoEn_new_logs', histogram_freq=0,
                          write_graph=True, write_images=False)

# introducing noise
noise_factor = 0.5
x_train_noisy = x_train + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_train.shape)
x_test_noisy = x_test + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_test.shape)

hist = autoencoder.fit(x_train_noisy, x_train,
                       epochs=10,
                       batch_size=128,
                       shuffle=True,
                       validation_data=(x_test_noisy, x_test))

prediction = autoencoder.predict(x_test_noisy)

plt.imshow(x_test[0].reshape(28, 28))
plt.show()
plt.imshow(prediction[0].reshape(28, 28))
plt.show()
