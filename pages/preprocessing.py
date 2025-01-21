import streamlit as st
import pandas as pd
def show_preprocessing():
    filepath = './static/dataset-stroke.csv'
    train_data = pd.read_csv((filepath), sep=',', header=0)
    df = pd.DataFrame(train_data)
    

    st.title('Preprocessing and Analysis on Fake Data')
    st.header('1. Preprocessing')
