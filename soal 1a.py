# m al faiz putra jalasenandra
# 21091397072

# Sal no 1a : Single Neuron

# Mengimport Library numpy, dan memberi inisial
import numpy as np

# Layer input 10 features
inputs = [1.1, 1.4, 2.0, 2.7, 3.0, 3.8, 4.0, 4.5, 5.0, 5.9]
weights = [0.6, 0.9, 1.6, 1.9, 2.5, 2.8, 3.0, 4.3, 4.6, 5.0]

# Neuron 1
bias = 4.0

outputs = np.dot(weights, inputs) + bias
print(outputs)