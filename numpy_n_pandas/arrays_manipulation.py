import numpy as np

a1 = np.array([1, 2, 3])
a2 = np.array([[1, 2.0, 3.3 ],
              [4, 5, 6.5]])
print(a1)

ones = np.ones(3)
#e.g. 1
print(ones + a1)

#e.g. 2
print(a1 - ones)

#e.g. 3
print(a1 * ones)

#e.g. 4
print(a2 ** 2)

#e.g. 5
np.square(a2)

#e.g. 6
print(a2 / 2)

#e.g. 7
print(np.exp(a2))
#e.g. 8
print(np.log(a1))
