import pandas as pd
import numpy as np

df = pd.read_csv('titanic.csv')

print(df['Age']>35)
print(df[df['Pclass'].isin([2,3])]) #isin operator
print(df[(df['Pclass'] == 2) | (df['Pclass'] == 3)]) #does the same work as isin operator
print(df[df['Age'].notna()])# Age data is not null
# Names of the passengers older than 35 years
print(df.loc[df['Age']>30,['PassengerId','Name','Survived','Age']])
print(df.describe())
#loc last index is included and iloc last index is not included
#iloc the last index is stricly not include
print(df.iloc[0:3,0:3]) 
print(df.loc[0:3,['PassengerId','Survived','Pclass']])
print(df.describe())
print(df.agg({
    'Age' : ['min','max','median','skew'], #instead of predifined statistics i can pic some important ones and get it done
    'Fare': ['min','max','median','mean']
}))
df.rename(columns=str.lower,inplace=True)
print(df.columns)
print(df[['sex','age']].groupby('sex').mean())
print(df.groupby('sex').mean(numeric_only=True))
print(df.groupby(['sex','pclass'])[['age','fare']].mean())
print(df.groupby('pclass')['pclass'].count())
print(df.groupby('pclass').mean(numeric_only=True))
#value_counts
#use the dropna arguement
print(df['pclass'].value_counts(dropna=True))
print(df['sex'].value_counts())
#long form of value_counts
#size includes the nan values count doesn't include the nan values
print(df.groupby('pclass')['pclass'].size())
print(df.groupby('sex')['age'].count())
print(df.groupby('sex')['age'].size())
print(df.sort_values('age').head())
print(df.sort_values(['pclass','age']).head())
print(df.sort_values(['pclass','age'],ascending=False).head())
print(df.sort_values(['age','pclass']).head())
print(df.sort_values(['age','pclass'],ascending=False).head())

a = np.floor(10*np.random.rand(2,12))
print(a)
print(np.hsplit(a,3)) #hsplit