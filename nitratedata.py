import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv('nitratedata.csv',parse_dates=['date.utc'])
df2 = pd.read_csv('particulatematter.csv',parse_dates=['date.utc'])
data1 = df1.drop(columns=['unit'])
data2 = df2.drop(columns=['unit'])
print(data1.head())
print(data2.head())
print(data1['city'].value_counts())
data12 = pd.concat([data1,data2],axis=0,keys=['NO2','PM25'])
print(data12)
print(data12['date.utc'].min())
print(data12['date.utc'].max())
print(data12['date.utc'].max() - data12['date.utc'].min())
print(data12['date.utc'].dt.month)