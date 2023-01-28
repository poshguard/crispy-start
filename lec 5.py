import numpy as np

# Same array as slide in video
a1 = np.array([[1, 2.0, 3.3 ],
              [4, 5, 6.5]])

print(a1)
print(type(a1))

#2

ones = np.ones((2,3))
print(ones)
ones.dtype

#3
zeros = np.zeros((2, 3))
print(zeros)

#4
range_array = np.arrange(0, 10, 2)

#
random_array = np.random.randint(0, 10, size=(3, 5))
random_array
