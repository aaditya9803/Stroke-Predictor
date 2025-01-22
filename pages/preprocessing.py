import streamlit as st


def show_preprocessing():

    # st.markdown("""
    # <style>
    # .stMarkdown { margin-bottom: 5px; }  /* Reduce bottom margin */
    # </style>
    # """, unsafe_allow_html=True)

    st.title('Preprocessing, ML Models, and Analysis on Fake Data')
    st.header(" ")
#Preprocessing
    st.header('1. Preprocessing')
#Null Values
    st.subheader('1.1. Null Values')
    st.code("df['bmi'].isnull().sum()")
    st.markdown(f"There were 201 Null values in the bmi column")
    st.code("df['bmi'].fillna(df['bmi'].mean(), inplace=True)")
    st.markdown(f"These Null values were then replaced by the mean(28.89) of the column")



# Label Encoder
    st.subheader(" ")
    st.subheader('1.2. Label Encoder')
    st.code("""
        label_encoder = LabelEncoder()
        columns_to_label = ['gender', 'ever_married', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
        for column in columns_to_label:
            df[column] = df[column].astype(str)
            df[column] = label_encoder.fit_transform(df[column])
        """)

    st.markdown("The non-numerical values in the dataframe was encoded as numerical values in the following ways:")
    
    st.code("""
    
        • Column: gender

        | Female → 0 | | Male → 1 | | Other → 2 |

        • Column: ever_married

        | No → 0 | | Yes → 1 |

        • Column: work_type

        | Govt_job → 0 | | Never_worked → 1 | | Private → 2 | | Self-employed → 3 | | children → 4 |

        • Column: Residence_type

        | Rural → 0 | | Urban → 1 |

        • Column: smoking_status

        | Unknown → 0 | | formerly smoked → 1 | | never smoked → 2 | | smokes → 3 |    
            
    
    """)

# OverSampling and UnderSampling
    st.subheader(" ")
    st.subheader('1.3. Oversampling/Undersampling')
    st.markdown("There is class imbalance in the dataframe:")
    st.markdown(f"• stroke == 0 is 4861")
    st.markdown(f"• stroke == 1 is 249")
    st.code("""
            over = SMOTE(sampling_strategy = 1)
            under = RandomUnderSampler(sampling_strategy = 0.1)
            steps = [('under', under),('over', over)]
            pipeline = Pipeline(steps=steps)
            X, y = pipeline.fit_resample(X, y)
            """)
    st.markdown("So, the stroke negative class was halved using RandomUnderSampler() and stroke positive class was Doubled using SMOTE()")
    st.markdown("When the dataframe is balanced, it looks as follows")
    st.markdown(f"• stroke == 0 is 2490")
    st.markdown(f"• stroke == 1 is 2490")



    st.header(" ")
    st.header("2. Machine Learning Models")
#SVM
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
    st.subheader(" ")
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
    st.subheader(" ")
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
    st.markdown("Note: Since the final model was trained on whole dataframe, higher values on performance report means the data is already seen which doesn't implies that the model is overfitting")


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
    st.markdown("Note: Since the final model was trained on whole dataframe, higher values on performance report means the data is already seen which doesn't implies that the model is overfitting")

