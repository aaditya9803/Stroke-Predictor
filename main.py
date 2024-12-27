import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filepath = 'laptop_price - dataset.csv'

st.title('Information about the dataset')

train_data = pd.read_csv((filepath), sep=',', header=0)
df = pd.DataFrame(train_data)
st.write('Head of the dataset:')
st.write(df.head())
st.write('Description of the numerical columns of the dataset:')
st.write(df.describe())
st.write('Companies in the dataset:')
st.write(df['Company'].unique())
st.write('CPU types in the dataset:')
st.write(df['CPU_Type'].value_counts())
# df.isnull().sum()

st.write('Distribution of Companies:')
plt.figure(figsize=(20, 6))
sns.histplot(df['Company'], kde=True)
plt.title('Distribution of Companies')
plt.xlabel('Company')
plt.ylabel('Frequency')
st.pyplot(plt)