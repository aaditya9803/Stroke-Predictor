import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_information():

    filepath = './static/dataset-stroke.csv'

    st.title('Information about the dataset')

    train_data = pd.read_csv((filepath), sep=',', header=0)
    df = pd.DataFrame(train_data)
    df_stroke = df[df['stroke'] == 1]

    total_people_stroke = df_stroke.shape[0]

    # st.write(df_stroke.head())
##########################################################################
    st.header('1. Data Analysis on people who had a stroke')



    st.markdown("""
        <style>
            .stImage {
                display: flex;
                justify-content: flex-start;
                align-items: flex-start;
                width: 50%;
                margin-left: 160px;  /* Move chart to the right */
                margin-top: -105px;
            }
            }
        </style>
        """, unsafe_allow_html=True)
        
    st.subheader('1.1. Gender')

    # Gender
    stroke_females = df_stroke[df_stroke['gender'] == 'Female'].shape[0]
    stroke_males = df_stroke[df_stroke['gender'] == 'Male'].shape[0]
    percent_females_stroke = (stroke_females / total_people_stroke) * 100
    percent_males_stroke = (stroke_males / total_people_stroke) * 100
    st.write(f"Gender-wise stroke distribution:")
    st.write(f"• Female:  {percent_females_stroke:.2f}%")
    st.write(f"• Male:  {percent_males_stroke:.2f}%")

    # Gender Pie Chart
    gender_labels = ['Female', 'Male']
    gender_sizes = [percent_females_stroke, percent_males_stroke]
    fig, ax = plt.subplots(figsize=(5, 5), dpi=300)  # Adjusted size and dpi for clarity
    ax.pie(gender_sizes, labels=gender_labels, autopct='%1.2f%%', colors=['pink', 'skyblue'], startangle=90, 
        textprops={'fontsize': 15})  # Adjusted font size for labels
    # ax.set_title("Gender Distribution of people who had a stroke", fontsize=7)  # Adjusted font size for title
    ax.axis('equal')
    st.pyplot(fig)


    st.subheader('1.2. Hypertension')

    # Hypertension
    stroke_no_hypertension = df_stroke[df_stroke['hypertension'] == 0].shape[0]
    stroke_with_hypertension = df_stroke[df_stroke['hypertension'] == 1].shape[0]
    percent_no_hypertension = (stroke_no_hypertension / total_people_stroke) * 100
    percent_with_hypertension = (stroke_with_hypertension / total_people_stroke) * 100
    st.write(f"Hypertension-wise stroke distribution:")
    st.write(f"• No Hypertension:  {percent_no_hypertension:.2f}%")
    st.write(f"• Hypertension:  {percent_with_hypertension:.2f}%")

    # Hypertension Pie Chart
    hypertension_labels = ['No Hypertension', 'Hypertension']
    hypertension_sizes = [percent_no_hypertension, percent_with_hypertension]
    fig, ax = plt.subplots(figsize=(5, 5), dpi=300)  # Adjusted size and dpi for clarity
    ax.pie(hypertension_sizes, labels=hypertension_labels, autopct='%1.2f%%', colors=['blue', 'yellow'], startangle=90, 
        textprops={'fontsize': 15})  # Adjusted font size for labels
    ax.axis('equal')
    st.pyplot(fig)


    st.subheader('1.3. Marital Status')
    # Marital Status
    stroke_never_married = df_stroke[df_stroke['ever_married'] == 'No'].shape[0]
    stroke_married = df_stroke[df_stroke['ever_married'] == 'Yes'].shape[0]
    percent_never_married = (stroke_never_married / total_people_stroke) * 100
    percent_married = (stroke_married / total_people_stroke) * 100
    st.write(f"Marital Status-wise stroke distribution:")
    st.write(f"• Never Married:  {percent_never_married:.2f}%")
    st.write(f"• Married:  {percent_married:.2f}%")

    # Marital Status Pie Chart
    marital_labels = ['Never Married', 'Married']
    marital_sizes = [percent_never_married, percent_married]
    fig, ax = plt.subplots(figsize=(5, 5), dpi=300)
    ax.pie(marital_sizes, labels=marital_labels, autopct='%1.2f%%', colors=['lightcoral', 'gold'], startangle=20, 
        textprops={'fontsize': 15})
    ax.axis('equal')
    st.pyplot(fig)

    st.subheader('1.4. Residence Type')
    # Residence Type
    stroke_rural = df_stroke[df_stroke['Residence_type'] == 'Rural'].shape[0]
    stroke_urban = df_stroke[df_stroke['Residence_type'] == 'Urban'].shape[0]
    percent_rural = (stroke_rural / total_people_stroke) * 100
    percent_urban = (stroke_urban / total_people_stroke) * 100
    st.write(f"Residence Type-wise stroke distribution:")
    st.write(f"• Rural:  {percent_rural:.2f}%")
    st.write(f"• Urban:  {percent_urban:.2f}%")

    # Residence Type Pie Chart
    residence_labels = ['Rural', 'Urban']
    residence_sizes = [percent_rural, percent_urban]
    fig, ax = plt.subplots(figsize=(5, 5), dpi=300)
    ax.pie(residence_sizes, labels=residence_labels, autopct='%1.2f%%', colors=['lightgreen', 'grey'], startangle=90, 
        textprops={'fontsize': 15})
    ax.axis('equal')
    st.pyplot(fig)

    st.subheader('1.5. Heart Disease')
    # Heart Disease
    stroke_no_heart_disease = df_stroke[df_stroke['heart_disease'] == 0].shape[0]
    stroke_with_heart_disease = df_stroke[df_stroke['heart_disease'] == 1].shape[0]
    percent_no_heart_disease = (stroke_no_heart_disease / total_people_stroke) * 100
    percent_with_heart_disease = (stroke_with_heart_disease / total_people_stroke) * 100
    st.write(f"Heart Disease-wise stroke distribution:")
    st.write(f"• No Heart Disease:  {percent_no_heart_disease:.2f}%")
    st.write(f"• Heart Disease:  {percent_with_heart_disease:.2f}%")

    # Heart Disease Pie Chart
    heart_disease_labels = ['No Heart Disease', 'Heart Disease']
    heart_disease_sizes = [percent_no_heart_disease, percent_with_heart_disease]
    fig, ax = plt.subplots(figsize=(5, 5), dpi=300)
    ax.pie(heart_disease_sizes, labels=heart_disease_labels, autopct='%1.2f%%', colors=['lightpink', 'salmon'], startangle=90, 
        textprops={'fontsize': 15})
    ax.axis('equal')
    st.pyplot(fig)


    st.subheader('1.6. Work Type')
    # Work Type
    stroke_govt_job = df_stroke[df_stroke['work_type'] == 'Govt_job'].shape[0]
    stroke_never_worked = df_stroke[df_stroke['work_type'] == 'Never_worked'].shape[0]
    stroke_private = df_stroke[df_stroke['work_type'] == 'Private'].shape[0]
    stroke_self_employed = df_stroke[df_stroke['work_type'] == 'Self-employed'].shape[0]
    stroke_have_children = df_stroke[df_stroke['work_type'] == 'children'].shape[0]
    percent_govt_job = (stroke_govt_job / total_people_stroke) * 100
    percent_never_worked = (stroke_never_worked / total_people_stroke) * 100
    percent_private = (stroke_private / total_people_stroke) * 100
    percent_self_employed = (stroke_self_employed / total_people_stroke) * 100
    percent_have_children = (stroke_have_children / total_people_stroke) * 100
    st.write(f"Work Type-wise stroke distribution:")
    st.write(f"• Government Job:  {percent_govt_job:.2f}%")
    st.write(f"• Never Worked:  {percent_never_worked:.2f}%")
    st.write(f"• Private:  {percent_private:.2f}%")
    st.write(f"• Self-employed:  {percent_self_employed:.2f}%")
    st.write(f"• Have children:  {percent_have_children:.2f}%")

    # Work Type Pie Chart
    work_type_labels = ['Government Job', 'Never Worked', 'Private', 'Self-employed', 'Have children']
    work_type_sizes = [percent_govt_job, percent_never_worked, percent_private, percent_self_employed, percent_have_children]
    fig, ax = plt.subplots(figsize=(5, 5), dpi=300)
    ax.pie(work_type_sizes, labels=work_type_labels, autopct='%1.2f%%', startangle=90, 
        colors=['purple', 'pink', 'lightblue', 'yellow', 'green'], textprops={'fontsize': 15})
    ax.axis('equal')
    st.pyplot(fig)



    st.subheader('1.7. Smoking Status')
        # Smoking Status
    stroke_unknown = df_stroke[df_stroke['smoking_status'] == 'Unknown'].shape[0]
    stroke_formerly_smoked = df_stroke[df_stroke['smoking_status'] == 'formerly smoked'].shape[0]
    stroke_never_smoked = df_stroke[df_stroke['smoking_status'] == 'never smoked'].shape[0]
    stroke_smokes = df_stroke[df_stroke['smoking_status'] == 'smokes'].shape[0]
    percent_unknown = (stroke_unknown / total_people_stroke) * 100
    percent_formerly_smoked = (stroke_formerly_smoked / total_people_stroke) * 100
    percent_never_smoked = (stroke_never_smoked / total_people_stroke) * 100
    percent_smokes = (stroke_smokes / total_people_stroke) * 100
    st.write(f"Smoking Status-wise stroke distribution:")
    st.write(f"• Unknown:  {percent_unknown:.2f}%")
    st.write(f"• Formerly Smoked:  {percent_formerly_smoked:.2f}%")
    st.write(f"• Never Smoked:  {percent_never_smoked:.2f}%")
    st.write(f"• Smokes:  {percent_smokes:.2f}%")

    # Smoking Status Pie Chart
    smoking_status_labels = ['Unknown', 'Formerly Smoked', 'Never Smoked', 'Smokes']
    smoking_status_sizes = [percent_unknown, percent_formerly_smoked, percent_never_smoked, percent_smokes]
    fig, ax = plt.subplots(figsize=(5, 5), dpi=300)
    ax.pie(smoking_status_sizes, labels=smoking_status_labels, autopct='%1.2f%%', startangle=90, 
        colors=['gray', 'lightblue', 'lightgreen', 'orange'], textprops={'fontsize': 15})
    ax.axis('equal')
    st.pyplot(fig)
