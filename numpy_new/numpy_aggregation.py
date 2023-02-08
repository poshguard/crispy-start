#AGGREGATION = performing the same operation on a number of things
import numpy as np
import pandas as pd

listy_list = [1, 2, 3]

print(type(listy_list))
print(sum(listy_list))

#Use pythons method sum() python on data types , use numpy methods on numpy arrays np.sum()

massive_array = np.random.random(100000)
massive_array.size #checks the size

print(massive_array[:100])

sum(massive_array)

print(np.sqrt(np.var(listy_list)))

#   STANDARD DEVIATION AND VARIANCE

high_var_array = np.array([1, 100, 200, 300, 4000, 5000])
low_var_array = np.array([2, 4, 6, 8, 10])

print(np.var(high_var_array))
print(np.var(low_var_array))

#std check

print(np.std(high_var_array),np.std(low_var_array) )

# DOT PRODUCT

np.random.seed(0)

mat1 = np.random.randint(10, size=(5,3))
mat2 = np.random.randint(10, size=(5,3))
print(mat1)


print(mat2 * mat1)

mat3 = np.dot(mat1, mat2.T)
print(mat3)

#dot product example

sales_amounts = np.random.randint(20, size=(5,3))
weekly_sales = pd.DataFrame(sales_amounts, index=['Mon','Tue','Wed','Thur','Fri'],
                                            columns=['Almond', 'Peanut','Cashew'])
print(weekly_sales)

prices = np.array([10, 8 , 12])
