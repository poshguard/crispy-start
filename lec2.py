import pandas as pd

car_sales = pd.read_csv('/Users/ulugbek_turaev/Desktop/sample_project/car-sales.csv')
print(car_sales)

car_sales.to_csv("exported-car-sales.csv", index=False)
exported_car_sales = pd.read_csv("exported-car-sales.csv")
print(exported_car_sales)
