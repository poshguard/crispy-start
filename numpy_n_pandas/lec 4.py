import pandas as pd

car_sales = pd.read_csv('/Users/ulugbek_turaev/Desktop/sample_project/car-sales.csv')
seats_colums = pd.Series([5, 5, 5, 5, 5])

car_sales["Seats"] = seats_colums


car_sales["Seats"].fillna(5, inplace=True)

# Column from Python list

fuel_economy = [7.5, 9.2, 5.0, 9.6, 8.7, 4.7, 7.6, 8.7, 3.0, 4.5]
car_sales["Fuel per 100KM"] = fuel_economy



car_sales["Total fuel used"] = car_sales["Odometer (KM)"]/100 * car_sales['Fuel per 100KM']



# Create a column from a single value

car_sales = car_sales.drop('Total fuel used', axis=1)
print(car_sales)

car_sales.sample(frac=1)

car_sales_shuffled = car_sales.sample(frac=1)

