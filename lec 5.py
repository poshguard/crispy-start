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
random_array = np.random.rand(5, 3)
print(random_array)

#5
random_array1 = np.random.randint(10, size=(5, 3))
print(random_array1)
