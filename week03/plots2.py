#histograms

import numpy as np
import matplotlib.pyplot as plt

'''
np.random.seed(1)
normdata = np.random.normal(size=10000)

plt.hist(normdata)
plt.show()
'''
fruit = np.array(['apples','bananas', 'oranges'])
numbers = np.array([23,77,500])

plt.pie(numbers, labels = fruit)
plt.savefig('lecture2')