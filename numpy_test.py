import numpy as np
from matplotlib import pyplot as plt

# print(np.arange(10))
# plt.scatter(np.arange(100), np.random.randint(0, 10, 100))
# plt.show()

def normal_distribution():
    x = np.random.normal(loc=1, scale=2, size=(2, 3))
    return x