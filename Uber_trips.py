#importing all necessary modules
import numpy as na
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# importing data set
ds = pd.read_csv("UberDataset.csv")

# data processing
ds.fillna({"PURPOSE":"Not"}, inplace=True)

ds['START_DATE'] = pd.to_datetime(ds['START_DATE'], errors='coerce')
ds['END_DATE'] = pd.to_datetime(ds['END_DATE'], errors='coerce')


ds['date'] = pd.DatetimeIndex(ds['START_DATE']).date
ds['time'] = pd.DatetimeIndex(ds['START_DATE']).hour

#changing into categories of day and night
ds['day-night'] = pd.cut(x=ds['time'],bins = [0,10,15,19,24],labels = ['Morning','Afternoon','Evening','Night'])

ds.dropna(inplace=True)
ds.drop_duplicates(inplace=True)
print(ds)

# Data Visuali9sation
sns.countplot(ds['CATEGORY'])
plt.savefig("Category_wise_countplot.png")

sns.countplot(ds['PURPOSE'])
plt.savefig("Purpose_wise_countplot.png")

sns.countplot(ds['day-night'])
plt.savefig("Day_Night_wise_countplot.png")

sns.countplot(data=ds, x='PURPOSE', hue='CATEGORY')
plt.savefig("Catagory_wise.png")