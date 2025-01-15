import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_information():
    filepath = './static/dataset-stroke.csv'

    st.title('Information about the dataset')

    train_data = pd.read_csv((filepath), sep=',', header=0)
    df = pd.DataFrame(train_data)
    st.write('Head of the dataset:')
    st.write(df.head())
    st.write('Description of the numerical columns of the dataset:')
    st.write(df.describe())

    # df.isnull().sum()

    st.write('Distribution of BMI:')
    plt.figure(figsize=(20, 6))
    sns.histplot(df['bmi'], kde=True)
    plt.title('Distribution of BMI')
    plt.xlabel('BMI')
    plt.ylabel('Frequency')
    st.pyplot(plt)