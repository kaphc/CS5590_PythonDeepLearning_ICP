import pandas as pd
import matplotlib.pyplot as plt

plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (20, 15)

# import dataset
data = pd.read_csv('data/train.csv')
data.quality.describe()

# plot the data
garage_field = data['GarageArea']
sale_price = data['SalePrice']
plt.scatter(garage_field, sale_price, alpha=.70, color='r')
plt.xlabel('Garage_Field:Column')
plt.ylabel('Sale_Price:Target')
plt.show()

# filter outliers
data_without_outliers = data['GarageArea'] <= 1100
data = data[data_without_outliers]
data_without_outliers = data['GarageArea'] > 200
data = data[data_without_outliers]
data_without_outliers = data['GarageArea'] != 0
data = data[data_without_outliers]
data_without_outliers = data['SalePrice'] != 0
data = data[data_without_outliers]

garage_field = data['GarageArea']
sale_price = data['SalePrice']
plt.scatter(garage_field, sale_price, alpha=.70, color='g')
plt.xlabel('Garage_Field:Column')
plt.ylabel('Sale_Price:Target')
plt.show()
