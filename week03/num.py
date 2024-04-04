import numpy as np
list=[1,2,3, 'string']
print(list)

numbers = np.array([1,2,3,4])
numbers = numbers * [1,2,3,4]
print(numbers)


rando = np.random.randint(100,200,30)
print(rando)
normalrando = np.random.normal(loc=50, scale = 20, size = 100)
print(normalrando)