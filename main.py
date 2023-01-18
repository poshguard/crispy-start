import pandas as pd

series = pd.Series(["BMW", "Toyota", "Honda"])
print(series)

colours = pd.Series(["Red", "Blue", "White"])
print(colours)

car_data = pd.DataFrame({"Car make": series, "Colour": colours})
print(car_data)

df = pd.read_csv('/Users/ulugbek_turaev/Desktop/sample_project/car-sales.csv')
print(df)
