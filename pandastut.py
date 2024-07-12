import pandas as pd 
import numpy as np

population = pd.Series([1,2.5,3,4,5])
print(population.sum(),'this is sum of the population')
print(population)
population.name = 'pop'
print(population)
print(population[2])
population.index = ['india','pak','usa','nig','sig']
print(population)
sample = pd.Series([3,4,5,6,7],index=['hi','hello','whatsup','next','sike'],name="sample")
print(sample)
print(sample['whatsup'])
print(sample.iloc[1]) #Can give numeric positions
print(sample.iloc[[2,3]])
print(sample[['hi','hello']])
print(sample['hello':'next']) #normal slicing in series include both the upperindex and the lower index
print(sample>4)
print(sample[sample>4])
print(sample*10) #vectorised operations
print(sample[sample>sample.mean()])
sample[sample>sample.mean()]=20
print(sample)
#pandas Dataframes
df1 = pd.DataFrame({'population':[1,2,3],'GDP':[17,15.5,14],'Continent':['Asia','Asia','North America']},columns=['population','GDP','Continent'])
print(df1)
df1.index = ['india','pak','USA']
print(df1)
print(df1.columns)
print(df1.index)
print(df1.info())
print(df1.shape)
print(df1.describe())
print('')
print(df1['population']) #entire column
print(df1.loc['india']) #loc alphabetical positioning
print(df1.iloc[-1]) #iloc numeric positioning
print(df1.iloc[-1]['GDP'])
print(df1.loc[['india','pak'],['population','GDP']])
print(df1.iloc[1:3])#iloc does not include the last index and loc includes the last index of the dataframe
print(sample)
print(sample.iloc[2:4])#omits the last index
print(df1.iloc[0:1,0:2])
print(df1.loc['india':'pak','population':'GDP']) 
print('')
print(df1['population']>1)
print(df1.loc[df1['population']>1,['population','Continent']])
print('')
print(df1.drop(['pak','USA']))
print(df1)
print(df1.drop(['USA','pak'],axis=0))
print(df1)
#broadcasting everything is immutable
crises = pd.Series([1,2],index=['population','GDP'])
print(crises)
print(df1[['population','GDP']]-crises)
#create a new column
langs = pd.Series(['Hindi','Urdu','English'],index=['india','pak','USA'])
print(langs)
df1['language']=langs
print(df1)
# df1['language']='english'
# print(df1)
print(df1.rename(columns={
    'GDP':'gross domestic product',
},
index={
    'pak':'pakistan',
    'USA':'United States'
}))
print(df1)
df1['Per capita'] = df1['GDP']/df1['population']
print(df1)
print(df1.head(2))
df2 = pd.read_csv('student.csv')
df3 = pd.read_csv('Samplecsvdatafile.csv')
df3.columns = ['date','price1','price2']
print(df3.head())
print(df3.shape)
print(df3.info())