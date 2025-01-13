import streamlit as st

def form_submit():
    print("submitted")

    

def show_home():
    if 'age'not in st.session_state:
        st.session_state.age = 0
    if 'gender'not in st.session_state:
        st.session_state.gender = ""
    if 'bmi'not in st.session_state:
        st.session_state.bmi = 0
    if 'hypertension'not in st.session_state:
        st.session_state.hypertension = ""
    if 'heart_disease'not in st.session_state:
        st.session_state.hear_disease = ""
    if 'avg_gulcose'not in st.session_state:
        st.session_state.avg_gulcose = 0
    if 'work_type'not in st.session_state:
        st.session_state.work_type = ""
    if 'married'not in st.session_state:
        st.session_state.married = ""
    if 'smokes'not in st.session_state:
        st.session_state.smokes = 0
    if 'residence'not in st.session_state:
        st.session_state.residence= ""
    if 'dont_know_gulcose' not in st.session_state:
        st.session_state.dont_know_gulcose = ""


    st.markdown("""
    <h1> Stroke Predictor </h1>
    <style type='text/css'>
        h1 {
            color: #2c3e50;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)


    with st.form(key='my_form'):
        
        st.subheader("Gender")
        st.session_state.gender = st.radio(
            "Select your gender:",
            ["Male", "Female"],
            index=None,
            help="Choose your gender from the options"
        )



        st.subheader("Age")
        st.session_state.age = st.slider("Select your age:",
                        min_value = 0,
                        max_value = 100,
                        value = st.session_state.age,
        )



        st.subheader("Bmi")
        st.session_state.bmi = st.slider("Select your bmi:",
                        min_value = 0,
                        max_value = 50,
                        value = st.session_state.bmi,
        )


        st.subheader("Hypertension")
        st.session_state.hypertension = st.radio(
            "Do you have Hypertension?",
            ["Yes", "No"],
            index=None,
            help="If you don't know just select 'No'"
        )


        st.subheader("Heart Disease")
        st.session_state.heart_disease = st.radio(
            "Do you have a heart disease?",
            ["Yes", "No"],
            index=None,
            help="If you don't know just select 'No'"
        )

        st.subheader("Average Gulcose Level")
        st.session_state.bmi = st.slider("Select your Average Gulcose level:",
                        min_value = 0,
                        max_value = 50,
                        value = st.session_state.bmi,
                        help = "if you don't know select I don't know"
        )
        st.session_state.dont_know_gulcose = st.checkbox(
            "I don't know my Gulcose Level",
        )


        st.subheader("Married Life")
        st.session_state.married = st.radio(
            "Are you married?",
            ["Yes", "No"],
            index=None,
            help="If you don't know just select 'No'"
        )


        st.subheader("Work Type")
        st.session_state.work_type = st.radio(
            "Select your work type",
            ["Private", "Self-employed", "Have children", "Government Job", "Never Worked"],
            index=None,
        )

        
        st.subheader("Residence Type")
        st.session_state.residence = st.radio(
            "Select your Residence type",
            ["Urban", "Rural"],
            index=None,
        )

        st.subheader("Smoking Status")
        st.session_state.smokes = st.radio(
            "What kind of smoker are you?",
            ["Smokes", "Formerly Smoked", "Never Smoked", "Unknown"],
            help="Select Unknown if you aren't sure",
            index=None,
        )







        st.subheader("Submit")
        # if submit_button:
        #     st.write(f"Form submitted with gender: {gender} and age: {st.session_state.age}")
        submit_button = st.form_submit_button(label='Submit') #, onclick=form_submit
