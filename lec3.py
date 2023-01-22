import pandas as pd

#1
car_sales_missing = pd.read_csv('/Users/ulugbek_turaev/Desktop/sample_project/car-sales-missing-data.csv')
print(car_sales_missing)
car_sales_missing["Odometer"].mean()

car_sales_missing["Odometer"] = car_sales_missing["Odometer"].fillna(car_sales_missing["Odometer"].mean())

print(car_sales_missing)

car_sales_missing = car_sales_missing.dropna(inplace=True)
print(car_sales_missing)

car_sales_missing = pd.read_csv('exported-car-sales.csv')
print(car_sales_missing)

car_sales_missing_dropped = car_sales_missing.dropna()

car_sales_missing_dropped.to_csv("car-sales-missing-dropped.csv")
