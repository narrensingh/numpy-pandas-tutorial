import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('airquality.csv',index_col=0)
#plots with legends to give a quick overview dataframe.plot()
#dataframe.plots.scatter() --> scatter plot
print(df.head())
df['london_mg_per_cubic'] = df['station_london']*1.23
print(df.head())
df['rotio_paris_london'] = (df['station_paris']/df['station_london'])
print(df.head())
df.rename(
    columns={
        'station_antwerp':'Antwerp',
        'station_paris' : 'Paris',
        'station_london':'London',
    },inplace=True
)
print(df.head())
