

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/content/ecommerce_customers_unit1.csv')
df

df.tail()

df.head()

df.describe()

df.shape

df.info()

df.dtypes

df=df.convert_dtypes()
df.dtypes

df.columns

df.loc[2].value_counts

df.sample(5)

df_missing=df.isnull().sum()
df_missing

df['age']=df['age'].fillna(df['age'].mean())
df['total_spent']=df['total_spent'].fillna(df['total_spent'].mean())
df['gender']=df['gender'].fillna(df['gender'].mode()[0])
df['device_type']=df['device_type'].fillna(df['device_type'].mode()[0])
df['country']=df['country'].fillna(df['country'].mode()[0])
df['preferred_category']=df['preferred_category'].fillna(df['preferred_category'].mode()[0])

df_missing=df.isnull().sum()
df_missing

df['age'].value_counts()

df.min()

df.max()

df.corr(numeric_only=True)

df.std(numeric_only=  True)

df1=df.duplicated().sum()
df.drop_duplicates(inplace=True)

plt.hist(df['Valuation (M)'],bins=20)
plt.xlabel('Valuation')
plt.ylabel('Funding')
plt.title('Histogram')
plt.show()