import pandas as pd

#1
car_sales = pd.read_csv('/Users/ulugbek_turaev/Desktop/sample_project/car-sales.csv')
print(car_sales)

#2
car_sales.to_csv("exported-car-sales.csv", index=False)
exported_car_sales = pd.read_csv("exported-car-sales.csv")
print(exported_car_sales)

#3
print(car_sales.dtypes)

#4
print(car_sales.columns)

#5
car_columns = car_sales.columns
print(car_columns)

#6


#7
car_prices =  pd.Series([3000, 1500, 111250])
car_prices.mean()

car_sales.sum()
car_sales["Doors"].sum()

print(car_sales.loc[3])

print(car_sales.iloc[5])

print(car_sales.loc[:4])

#8
car_sales[car_sales["Make"] == 'Toyota']

#9
car_sales['Make'] = car_sales['Make'].str.lower()
print(car_sales)
