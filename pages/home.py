import streamlit as st

def show_home():

    st.markdown("""
    <h1> Stroke Predictor </h1>
    <style type='text/css'>
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        }

        .container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 10px;
        padding: 10px;
        }

        .box {
        border: 2px solid red;
        padding: 20px;
        text-align: center;
        height: 150px;
        }

        @media screen and (max-width: 768px) {
        .container {
            grid-template-columns: repeat(2, 1fr);
        }
        }

        @media screen and (max-width: 480px) {
        .container {
            grid-template-columns: 1fr;
        }
        }
    </style>
    """, unsafe_allow_html=True)


    st.markdown('<div class="container">', unsafe_allow_html=True)



    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.subheader("Gender")
    gender = st.radio(
        "Select your gender:",
        ["Male", "Female", "Other"],
        index=None,
        help="Choose your gender from the options"
    )
    st.markdown('</div>', unsafe_allow_html=True)



    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.subheader("Age")
    age = st.slider("Select your age:",
                    min_value = 0
    )
    st.markdown('</div>', unsafe_allow_html=True)


    st.markdown('</div>', unsafe_allow_html=True)
