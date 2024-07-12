#number missing category missing or any thing else
import numpy as np
import pandas as pd

# age => 170 years not possible
# domains a range
# filling the missing the values
series1 = pd.Series([1,2,3,np.nan,4,5,np.nan])
# nan => for pandas and numpy
print(pd.isnull(np.nan))
print(pd.isnull(pd.Series([1,2,3,np.nan,4,5,np.nan])))
print(pd.notnull(pd.Series([1,2,3,np.nan,4,5,np.nan])))
print(pd.notnull(series1).sum())
print(series1[pd.notnull(series1)])
print(series1[series1.isnull()])

df = pd.DataFrame({
    'columnA':[1,np.nan,np.nan,4],
    'columnB':[3,np.nan,2,1],
    'columnC':[1,2,3,4]
})
print(df)
print(df.iloc[1].isnull())
print(df.notnull().sum())
print(df.dropna())
print(df.dropna(axis=1))
print(df.dropna(thresh=3,axis=1)) #thresh =2 it mush have atleast 2 valid values depending on the axis passed throught as param , by default dropna takes axis as 0
print(df)
print(df.fillna(df.mean())) # the mean wont calculate nan values as items it ommits them***
# for eg: 1,nan,nan,4 => 1+4/2 = 2.5
# dropna isnull notnull fillna etc
# any and all
print(series1.notnull().all())

df = pd.DataFrame({
    'sex' : ['m','f','f','f','m','d','?','h'],
    'age':[29,30,24,290,25,54,34,2]
})
print(df)
print(df['sex'].unique())
print(df['sex'].value_counts()) # counts each of individual unique values
# we know that 290 in invalid age for any human
df.loc[df['age']>100,'age']  = df.loc[df['age']>100,'age']/10
print(df.iloc[1,1])
#duplicate data drop_duplicate
print(df.drop_duplicates(subset=['sex']))
print(df['age'].duplicated())
## string methods
#df['data'].str.method => split contains strip replace 