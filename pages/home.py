import streamlit as st

def form_submit():
    # Access form data from session state
    age = st.session_state.age
    gender = st.session_state.gender
    bmi = st.session_state.bmi
    hypertension = st.session_state.hypertension
    heart_disease = st.session_state.heart_disease
    avg_gulcose = st.session_state.avg_gulcose
    work_type = st.session_state.work_type
    married = st.session_state.married
    smokes = st.session_state.smokes
    residence = st.session_state.residence
    dont_know_gulcose = st.session_state.dont_know_gulcose

    # Print values for debugging
    print("\nSubmitted Data:")
    print(age, gender, bmi, hypertension, heart_disease, avg_gulcose, work_type, married, smokes, residence, dont_know_gulcose)

# Function to show the form
def show_home():
    if "initialized" not in st.session_state:
        st.session_state.update({
            "age": 0,
            "gender": "Male",
            "bmi": 0,
            "hypertension": "No",
            "heart_disease": "No",
            "avg_gulcose": 0,
            "work_type": "Private",
            "married": "No",
            "smokes": "Never Smoked",
            "residence": "Urban",
            "dont_know_gulcose": False,
            "initialized": True,
        })

    st.markdown("""
    <h1> Stroke Predictor </h1>
    <style>
        h1 { color: #2c3e50; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

    # Form to collect inputs
    with st.form(key="user_form"):
        st.radio("Select your gender:", ["Male", "Female"], key="gender")
        st.slider("Select your age:", min_value=0, max_value=100, key="age")
        st.slider("Select your BMI:", min_value=0, max_value=50, key="bmi")
        st.radio("Do you have Hypertension?", ["Yes", "No"], key="hypertension")
        st.radio("Do you have a heart disease?", ["Yes", "No"], key="heart_disease")
        st.slider("Select your Average Glucose level:", min_value=0, max_value=300, key="avg_gulcose")
        st.checkbox("I don't know my Glucose Level", key="dont_know_gulcose")
        st.radio("Are you married?", ["Yes", "No"], key="married")
        st.radio("Select your work type:", ["Private", "Self-employed", "Have children", "Government Job", "Never Worked"], key="work_type")
        st.radio("Select your Residence type:", ["Urban", "Rural"], key="residence")
        st.radio("What kind of smoker are you?", ["Smokes", "Formerly Smoked", "Never Smoked", "Unknown"], key="smokes")

        # Submit button
        submitted = st.form_submit_button("Submit")
        if submitted:
            form_submit()

