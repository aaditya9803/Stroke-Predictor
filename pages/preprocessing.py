import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from collections import Counter
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline

def show_preprocessing():

    # st.markdown("""
    # <style>
    # .stMarkdown { margin-bottom: 5px; }  /* Reduce bottom margin */
    # </style>
    # """, unsafe_allow_html=True)
    filepath = './static/dataset-stroke.csv'
    train_data = pd.read_csv((filepath), sep=',', header=0)
    df = pd.DataFrame(train_data)  #this is orginal dataframe
    df_stroke = df[df['stroke'] == 1] # this is dataframe of rows only where stroke was 1
    df_stroke = df_stroke.drop(columns='id')


    st.title('Preprocessing, ML Models, and Analysis on Fake Data')
    st.header('1. Preprocessing')


    st.subheader('1.1. NaN Values')
    df['bmi']=df['bmi'].fillna(df['bmi'].mean())
    st.code("df['bmi'].isnull().sum()")
    st.markdown(f"There were {df['bmi'].isnull().sum()} Null values in the bmi column")
    st.code("df['bmi'].fillna(df['bmi'].mean(), inplace=True)")
    st.markdown(f"These Null values were then replaced by the mean({df['bmi'].isnull().sum()}) of the column")

    st.subheader('1.2. Label Encoder')
    st.code("""
        label_encoder = LabelEncoder()
        columns_to_label = ['gender', 'ever_married', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
        for column in columns_to_label:
            df[column] = df[column].astype(str)
            df[column] = label_encoder.fit_transform(df[column])
        """)



    st.markdown("The non-numerical values in the dataframe was encoded as numerical values in the following ways:")
    label_encoder = LabelEncoder()
    columns_to_label = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
    for column in columns_to_label:
        label_encoder.fit(df[column])
        st.markdown(f"• Column: {column}")
        rows = []
        for label, encoded in zip(label_encoder.classes_, range(len(label_encoder.classes_))):
            rows.append(f"|    {label} → {encoded}    |")
        st.markdown("\n".join(rows), unsafe_allow_html=True)

    #To actually label for sampling and to not be shown on webpage
    # df_stroke is labelled here aswell
    columns_to_label = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
    for column in columns_to_label:
        df[column] = df[column].astype(str)
        df_stroke[column] = df_stroke[column].astype(str)
        df[column] = label_encoder.fit_transform(df[column])
        df_stroke[column] = label_encoder.fit_transform(df_stroke[column])



    st.subheader('1.3. Oversampling/Undersampling')
    y = df['stroke']
    X = df.drop(columns='stroke')
    st.markdown("There is class imbalance in the dataframe:")
    st.markdown(f"• stroke == 0 is {Counter(y)[0]}")
    st.markdown(f"• stroke == 1 is {Counter(y)[1]}")
    st.code("""
            over = SMOTE(sampling_strategy = 1)
            under = RandomUnderSampler(sampling_strategy = 0.1)
            steps = [('under', under),('over', over)]
            pipeline = Pipeline(steps=steps)
            X, y = pipeline.fit_resample(X, y)
            """)
    st.markdown("So, the stroke negative class was halved using RandomUnderSampler() and stroke positive class was Doubled using SMOTE()")
    
    over = SMOTE(sampling_strategy = 1)
    under = RandomUnderSampler(sampling_strategy = 0.1)
    steps = [('under', under),('over', over)]
    pipeline = Pipeline(steps=steps)
    X, y = pipeline.fit_resample(X, y)

    st.markdown("When the dataframe is balanced, it looks as follows")
    st.markdown(f"• stroke == 0 is {Counter(y)[0]}")
    st.markdown(f"• stroke == 1 is {Counter(y)[1]}")


#SVM
    st.header(" ")
    st.header("2. Machine Learning Models")
    st.subheader("2.1. Support Vector Machine")

#Cross Fold Method SVM   
    st.markdown("##### 2.1.1 Cross Fold Method")
    st.code("""
        Average F1-score across 5 folds: 0.7648
        Average Accuracy across 5 folds: 0.7657
        Average Precision across 5 folds: 0.7701
        Average Recall across 5 folds: 0.7657
            """)

# Test Train Split SVM
    st.markdown("##### 2.1.2 Test-Train Split Method")
    st.code("""
        Final Model Accuracy: 0.7590
        Final Model Precision: 0.7625
        Final Model Recall: 0.7590
        Final Model F1-score: 0.7584
        Final Model Confusion Matrix:
                            [[353 148]
                            [ 92 403]]
            """)


#XGBoost model
    st.header(" ")
    st.subheader("2.2. XGBoost")
    st.markdown("**Note: Since the XGBoost Model seemed promising, it is primarily used in this project**")
# Cross Fold Method XGB
    st.markdown("##### 2.2.1 Cross Fold Method")
    st.code("""
        Average F1-score across 5 folds: 0.9223
        Average Accuracy across 5 folds: 0.9223
        Average Precision across 5 folds: 0.9232
        Average Precision across 5 folds: 0.9223
            """)
# Test-Train Split Method XGB
    st.subheader(" ")
    st.markdown("##### 2.2.2 Test-Train Split Method")
    st.code("""
        Model Accuracy: 0.9227
        Model Precision: 0.9233
        Model Recall: 0.9227
        Model F1-score: 0.9227
        Model Confusion Matrix:
                        [[453  48]
                        [ 29 466]]
        """)
    st.markdown("**Note: As the results with Cross Fold Method looked good, the whole dataframe was used to train the Final Model**")
    

#Testing the Final model with half of the dataset
    st.subheader(" ")
    st.markdown("##### 2.2.3 Testing the Final model with half of the dataset")
    st.code("""
            Accuracy: 0.9959839357429718
            Precision: 0.9959852053301071
            Recall: 0.9959839357429718
            F1-score: 0.9959839279700243
            Confusion Matrix:
            [[1237    6]
            [   4 1243]]
        """)
    st.markdown("Note: Since the final model was trained on whole dataframe, higher values on performance report means the data is already seen which doesn't implies that model is overfitting")


# Testing the Final model with only Stroke dataset
    st.subheader(" ")
    st.markdown("##### 2.2.4 Testing the Final model with only Stroke dataset (Where stroke==1)")
    st.code("""
            Accuracy: 0.9718875502008032
            Precision: 1.0
            Recall: 0.9718875502008032
            F1-score: 0.9857433808553971
            Confusion Matrix:
            [[  0   0]
            [  7 242]]
        """)
    st.markdown("Note: Since the final model was trained on whole dataframe, higher values on performance report means the data is already seen which doesn't implies that model is overfitting")