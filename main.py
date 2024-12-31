import streamlit as st
from pages.home import show_home
from pages.information import show_information
from pages.preprocessing import show_preprocessing
# st.sidebar.empty()

st.set_page_config(initial_sidebar_state="collapsed")


st.markdown("""
    <style>
        .css-1d391kg {visibility: hidden;}

        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        #stSidebar {visibility: hidden;} 
        [data-testid="collapsedControl"] {
        display: none
        }
            
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
        
        /* Navbar container styling */
        div[data-testid="stHorizontalBlock"] {
            background-color: #0066cc;
            width: 100vw;
            padding: 0;  /* Removed padding */
            display: flex;
            justify-content: center;
            gap: 0;  /* Removed gap */
            position: fixed;
            top: 0;
            left: 0;
            z-index: 999;
        }
        
        /* Button styling */
        .stButton button {
            background-color: transparent;
            color: white;
            border: 2px solid white;
            padding: 8px 30px;  /* Adjusted padding for square look */
            border-radius: 25px;
            font-size: 16px;
            font-weight: 500;
            min-width: 120px;
            height: 40px;  /* Fixed height */
            transition: all 0.3s;
            margin: 8px 0;  /* Added small vertical margin */
        }
        
        .stButton button:hover {
            background-color: white;
            color: #0066cc;
        }
        
        .main-content {
            margin-top: 56px;  /* Adjusted to match navbar height */
            padding: 0 2rem;
        }
        
        /* Responsive design */
        @media screen and (max-width: 768px) {
            .stButton button {
                padding: 6px 20px;
                min-width: 100px;
                height: 35px;
                font-size: 14px;
            }
        }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

if 'page' not in st.session_state:
    st.session_state.page = 'home'

with col1:
    if st.button("Home"):
        st.session_state.page = 'home'
with col2:
    if st.button("Information"):
        st.session_state.page = 'information'
with col3:
    if st.button("Preprocessing"):
        st.session_state.page = 'preprocessing'
with col4:
    if st.button("Contact"):
        st.session_state.page = 'contact'

st.markdown('<div class="main-content">', unsafe_allow_html=True)

if st.session_state.page == 'home':
    show_home()
elif st.session_state.page == 'information':
    show_information()
elif st.session_state.page == 'preprocessing':
    show_preprocessing()
elif st.session_state.page == 'contact':
    st.title("Contact")
    st.write("Get in touch with us")

st.markdown('</div>', unsafe_allow_html=True)

