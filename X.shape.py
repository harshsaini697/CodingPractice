import numpy as np

a = np.array([[1,2,3], [4,5,6]])
print(a.shape.__len__())

parameters = {"W1": 1,
                  "b1": 2,
                  "W2": 3,
                  "b2": 4}

print(parameters.get('W1'))