import streamlit as st


def show_preprocessing():

    st.title('Preprocessing, ML Models, and Effects of Fake Data')
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
    st.subheader(" ")
#SVM
    st.subheader("2.1. Support Vector Machine")
    st.markdown(" ")
    
#Cross Fold Method SVM   
    st.markdown("##### 2.1.1 Cross Fold Method")
    st.code("""

        _       precision   recall   f1-score   support
        Fold 1:
           0       0.79      0.71      0.75       502
           1       0.73      0.81      0.77       494
        Fold 2:
           0       0.75      0.70      0.72       488
           1       0.73      0.77      0.75       508            
        Fold 3:   
           0       0.82      0.67      0.74       509
           1       0.71      0.85      0.77       487
        Fold 4:
           0       0.78      0.70      0.74       506
           1       0.72      0.80      0.76       490
        Fold 5:
           0       0.79      0.71      0.75       485
           1       0.75      0.82      0.78       511
            """)

    st.code("""
        Average F1-score across 5 folds: 0.7530
        Average Accuracy across 5 folds: 0.7538
        Average Precision across 5 folds: 0.7577
        Average Recall across 5 folds: 0.7538
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
    st.subheader(" ")
# Cross Fold Method XGB
    st.markdown("##### 2.2.1 Cross Fold Method")
    st.code("""
        _      precision   recall   f1-score   support
        Fold 1:
           0       0.94      0.89      0.92       502
           1       0.90      0.94      0.92       494
        Fold 2:
           0       0.93      0.93      0.93       488
           1       0.93      0.93      0.93       508
        Fold 3:
           0       0.95      0.86      0.91       509
           1       0.87      0.95      0.91       487
        Fold 4:
           0       0.94      0.87      0.90       506
           1       0.87      0.94      0.91       490
        Fold 5:
           0       0.95      0.91      0.93       485
           1       0.92      0.95      0.94       511
            """)
    st.code("""
        Average F1-score across 5 folds: 0.9188
        Average Accuracy across 5 folds: 0.9189
        Average Precision across 5 folds: 0.9205
        Average Precision across 5 folds: 0.9189
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




#Fake Data
    st.header(" ")
    st.header('3. Fake Data')
    st.subheader(" ")
    st.subheader('3.1 Fake Data Generator')

    st.code("""
    a = []
    b = []
    for i in range(1000):
        a.append(random.choice(original_dataframe['column_a']))
        b.append(random.choice(original_dataframe['column_a']))
    fake_data = {
        "column_a": a,
        "column_b": b,
    }
    df_fakedata = pd.DataFrame(fake_data)
        """)
    st.markdown("Approach: Values from the original dataframe was picked  ***randomly*** to generate a dataframe with fake data")

#Effects of Fake data on Model
    st.subheader(" ")
    st.subheader("3.2 Effects of Fake Data on the Model Performance")
    st.markdown("Approach: Dataframe made with fake data was merged to the orginal dataframe")
    st.subheader(" ")
    st.markdown("##### 3.2.1 Cross Fold Method with XGBoost")
    st.code("""
        _      precision   recall   f1-score   support
        Fold 1:
           0       0.95      0.99      0.97      1162
           1       0.13      0.03      0.05        60
        Fold 2:
           0       0.96      0.99      0.98      1177
           1       0.08      0.02      0.03        45
        Fold 3:
           0       0.94      0.99      0.97      1150
           1       0.28      0.07      0.11        72
        Fold 4:
           0       0.95      0.99      0.97      1162
           1       0.24      0.07      0.10        60
        Fold 5:
           0       0.95      0.99      0.97      1157
           1       0.42      0.08      0.13        65
        """)
    st.markdown("Effect of fake data: It can be seen that the model performance for class 1 has significantly decreased")
    st.code("""
        Average F1-score across 5 folds: 0.9275
        Average Accuracy across 5 folds: 0.9439
        Average Precision across 5 folds: 0.9176
        Average Precision across 5 folds: 0.9439
    """)
    st.markdown("Since 'class 1' is insignificant, Average Model Performance is dominated by 'class 0'")
    
# Test Train Split Method with XGBoost
    st.subheader(" ")
    st.markdown("##### 3.2.2 Test Train Split Method with XGBoost")
    st.code("""
        Final Model Accuracy: 0.9427
        Final Model Precision: 0.9155
        Final Model Recall: 0.9427
        Final Model F1-score: 0.9235
        Final Model Confusion Matrix:
        [[1148    8]
        [  62    4]]
    """)
    st.markdown("""
        Effect of fake data: Even though the Acurracy, Precision, Recall, and F1 scores are dominated by the results of class 0,
                                the actual effect can be seen on Confusion Matrix where 62 of 'class 1' out of 66 were classified as False Negative.
                                While True Negative is just 4.
      """)

