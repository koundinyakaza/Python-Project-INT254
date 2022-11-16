# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 15:39:23 2022

@author: kound
"""

# import lib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# load data
df = pd.read_csv('C:/Users/kound/Downloads/SampleSuperstore.csv.xls')
df.head()
df.isnull().sum()
# check information
df.info()
df.describe()
# check duplicated values
df[df.duplicated(keep=False)]
# drop duplicated values
df.drop_duplicates(inplace=True)
df['Country'].unique()
# drop useless features like country because it contain only US and postal code
df.drop(['Country', 'Postal Code'], axis=1,inplace=True)
# look again to dataset
df.head()
import warnings
warnings.filterwarnings('ignore')
plt.figure(figsize=(15,20))
plt.subplot(4,2,1)
sns.distplot(df['Sales'])
plt.subplot(4,2,2)
sns.boxplot(df['Sales'])
plt.subplot(4,2,3)
sns.distplot(df['Quantity'])
plt.subplot(4,2,4)
sns.boxplot(df['Quantity'])
plt.subplot(4,2,5)
sns.distplot(df['Discount'])
plt.subplot(4,2,6)
sns.boxplot(df['Discount'])
plt.subplot(4,2,7)
sns.distplot(df['Profit'])
plt.subplot(4,2,8)
sns.boxplot(df['Profit'])
plt.show()
# The interquartile range (IQR) is the difference between the 75th and 25th percentile of the data. 
# It is a measure of the dispersion similar to standard deviation or variance, 
# but is much more robust against outliers 
percentile25 = df['Sales'].quantile(0.25)
print(percentile25)
percentile75 = df['Sales'].quantile(0.75)
print(percentile75)
print("Highest allowed",df['Sales'].mean() + 3*df['Sales'].std())
print("Lowest allowed",df['Sales'].mean() - 3*df['Sales'].std())
print("Highest allowed",df['Quantity'].mean() + 3*df['Quantity'].std())
print("Lowest allowed",df['Quantity'].mean() - 3*df['Quantity'].std())
print("Highest allowed",df['Discount'].mean() + 3*df['Discount'].std())
print("Lowest allowed",df['Discount'].mean() - 3*df['Discount'].std())
print("Highest allowed",df['Profit'].mean() + 3*df['Profit'].std())
print("Lowest allowed",df['Profit'].mean() - 3*df['Profit'].std())
# check correlation
sns.heatmap(df.corr(), cmap="Blues");
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
sns.barplot(x='Region', y='Profit', data=df, ax=ax[0])
sns.barplot(x='Region', y='Sales', data=df, ax=ax[1])
sns.barplot(x='Region', y='Discount', data=df, ax=ax[2])
plt.show()
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
sns.barplot(x='Category', y='Profit', data=df, ax=ax[0])
sns.barplot(x='Category', y='Sales', data=df, ax=ax[1])
sns.barplot(x='Category', y='Discount', data=df, ax=ax[2])
plt.show()
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
sns.barplot(x='Segment', y='Profit', data=df, ax=ax[0])
sns.barplot(x='Segment', y='Sales', data=df, ax=ax[1])
sns.barplot(x='Segment', y='Discount', data=df, ax=ax[2])
plt.show()
fig, ax = plt.subplots(1, 3, figsize=(18, 5))
sns.barplot(x='Ship Mode', y='Profit', data=df, ax=ax[0])
sns.barplot(x='Ship Mode', y='Sales', data=df, ax=ax[1])
sns.barplot(x='Ship Mode', y='Discount', data=df, ax=ax[2])
plt.show()
fig, ax = plt.subplots(1, 3, figsize=(18, 5))
sns.barplot(x='Quantity', y='Profit', data=df, ax=ax[0])
sns.barplot(x='Quantity', y='Sales', data=df, ax=ax[1])
sns.barplot(x='Quantity', y='Discount', data=df, ax=ax[2])
plt.show()
fig, ax = plt.subplots(1, 2, figsize=(15, 5))
sns.barplot(x='Discount', y='Sales', data=df, ax=ax[0])
sns.barplot(x='Discount', y='Profit', data=df, ax=ax[1])
plt.show()
sns.countplot(x='Category', data=df, order=df['Category'].value_counts().index);
plt.figure(figsize=(15, 5))
sns.countplot(x='Sub-Category', data=df, order=df['Sub-Category'].value_counts().index);
plt.xticks(rotation=90);
plt.show()
fig, ax = plt.subplots(figsize=(10, 5))
sns.scatterplot(x='Discount', y='Profit', hue='Category', data=df);
ax.legend(fontsize=12)
plt.show()
fig, ax = plt.subplots(figsize=(15, 5))
sns.barplot(x='Sub-Category', y='Profit', data=df);
plt.xticks(rotation=90)
ax.bar_label(ax.containers[0])
plt.show()
# group by with each state
states = df.groupby('State').sum().sort_values('Sales', ascending=False)
states.reset_index(inplace=True)
fig, ax = plt.subplots(figsize=(15, 5))
sns.barplot(x='State', y='Sales', data=states);
plt.xticks(rotation=90)
plt.show()
fig, ax = plt.subplots(figsize=(15, 5))
states = states.sort_values('Quantity', ascending=False)
sns.barplot(x='State', y='Quantity', data=states);
plt.xticks(rotation=90)
plt.show()
fig, ax = plt.subplots(figsize=(15, 5))
states = states.sort_values('Profit', ascending=False)
sns.barplot(x='State', y='Profit', data=states);
plt.xticks(rotation=90)
plt.show()
states= df.groupby(['State'])[['Sales', 'Profit']].sum()
states.sort_values("Profit", ascending=False).plot(kind = 'bar', figsize = (20,8))
plt.show()
states= df.groupby(['State']).sum().sort_values('Discount', ascending=False)
states.reset_index(inplace=True)

fig, ax = plt.subplots(figsize=(15, 5))
sns.barplot(x='State', y='Discount', data=states)
plt.xticks(rotation=90)
plt.show();
sns.stripplot(x="Category",y="Sub-Category",data=df)
plt.show()
