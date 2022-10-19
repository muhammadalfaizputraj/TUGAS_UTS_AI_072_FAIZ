import numpy as np

inputs = [1.0, 1.9, 2.3, 2.7, 3.0, 3.3, 4.0, 4.5, 5.3, 5.6]
weights = [
    [0.1, 0.4, 0.6, 0.8, 1.4, 1.7, 1.9, 2.5, 2.9, 3.0],
    [2.5, 2.8, 3.0, 3.8, 4.6, 4.8, 5.7, 5.8, 6.6, 6.8],
]

biases = [1.0, 2.7]

outputs = np.dot(weights, inputs) + biases
print(outputs)