import streamlit as st
from pages.home import show_home
from pages.information import show_information
from pages.preprocessing import show_preprocessing
from pages.chatbot import show_chatbot
import base64


robot_image_path = "static/robot.png"


# To incode the image into base 64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode("utf-8")
    return f"data:image/png;base64,{encoded_image}"


robot_image_base64 = get_base64_image(robot_image_path)





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
            background-color: #000000;
            width: 100vw;
            padding: 0;  
            display: flex;
            justify-content: center;
            gap: 0; 
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
            height: 40px; 
            transition: all 0.3s;
            margin: 8px 0; 
        }
        
        .stButton button:hover {
            background-color: white;
            color: #0066cc;
        }
        
        .main-content {
            margin-top: 56px;  /* Adjusted to match navbar height */
            padding: 0 2rem;
        }
        
 
        @media screen and (max-width: 768px) {
            /* Navbar layout on small screens 
            div[data-testid="stHorizontalBlock"] {
                display: flex !important;
                flex-direction: row !important;
                justify-content: space-between !important;
                gap: 5px !important; 
                flex-wrap: nowrap !important;  
                width: 100%;
                padding: 5px !important;
                box-sizing: border-box !important;
                overflow-x: auto;
            }

            /* Make columns smaller to fit all buttons */
            div[data-testid="stColumn"] {
                flex: 1 1 auto !important;
                max-width: 20% !important; /*column width */
                min-width: 15% !important; /*minimum width */
            }

            /* Button Styling for Smaller Screens */
            .stButton button {
                padding: 5px 12px !important;  
                min-width: 70px !important;  
                height: 30px !important; 
                font-size: 10px !important; 
                border-radius: 15px !important;  
                color: white !important;
                border: 2px solid white !important;
                background-color: transparent !important;
                visibility: visible !important;
                display: inline-block !important;
            }

            .stButton button:hover {
                background-color: white !important;
                color: #0066cc !important;
            }

            /* Adjust Specific Robot Button */
            div[data-testid="stHorizontalBlock"] > div:nth-of-type(3) button {
                width: 40px !important;
                height: 40px !important;
                background-repeat: no-repeat !important;
                background-position: center !important;
                background-size: contain !important;
                border: none !important;
                border-radius: 50% !important;
                visibility: visible !important;
            }

            /* Ensure buttons are horizontally aligned on smaller screens */
            @media screen and (max-width: 480px) {
                div[data-testid="stHorizontalBlock"] {
                    flex-direction: row !important;
                    justify-content: space-around !important; /* Spread out buttons evenly */
                    gap: 5px !important; 
                }

                }

            }
            
        }










        section[data-testid="stSidebar"] {
            display: none !important;
        }
        [data-testid="stSidebarCollapsedControl"] {
            display: none !important;
        }
        div[data-testid="stHorizontalBlock"] .stButton:first-child {
            margin-left: 0px; /* Adds gap before the first button */
        }

        div[data-testid="stHorizontalBlock"] > div:nth-of-type(3) button {
            # background-color: blue !important;
            color: transparent;
            background-color: transparent !important;
            background-repeat: no-repeat !important;
            background-position: center !important;
            background-size: contain !important;
            border: none !important;
            width: 60px !important;
            height: 60px !important;
            cursor: pointer !important;
            border-radius: 50% !important;
            position: absolute !important; /* Make the button position absolute */
            top: -20px; /* Adjust the vertical position */
            left: 45%; /* Adjust the horizontal position */
            transform: translate(-50%, -50%); 
            z-index: 10 !important; 
            min-width: 120px;
            height: 40px;  /* Fixed height */
            transition: all 0.3s;
            margin: 8px 0;
        }   

    </style>


#This is the working versions
""", unsafe_allow_html=True)



st.markdown('<div class="main-content">', unsafe_allow_html=True)
nav_placeholder = st.empty()  # Create a placeholder for the navigation bar
with nav_placeholder.container():
    col1, col2, col3, col4, col5 = st.columns(5)

    if 'page' not in st.session_state:
        st.session_state.page = 'home'

    with col1:
        if st.button("Home"):
            st.session_state.page = 'home'
    with col2:
        if st.button("Info."):
            st.session_state.page = 'information'
    with col3:
        # <a href="#" onclick="fetch('/?page=chatbot')">
        # cursor: pointer;
        st.markdown(f"""
            <img src="{robot_image_base64}" alt="Chatbot" style="width: 50px; height: 50px; margin-left: 35%">
        """, unsafe_allow_html=True)

        if st.button(""):
            st.session_state.page = 'chatbot'

    with col4:
        if st.button("Pre."):
            st.session_state.page = 'preprocessing'
    with col5:
        if st.button("Cont."):
            st.session_state.page = 'contact'
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="content">', unsafe_allow_html=True)

if st.session_state.page == 'home':
    show_home()
elif st.session_state.page == 'information':
    show_information()
elif st.session_state.page == 'preprocessing':
    show_preprocessing()
elif st.session_state.page == 'chatbot':
    show_chatbot()
elif st.session_state.page == 'contact':
    st.title("Contact")
    st.write("Get in touch with us")
        

st.markdown('</div>', unsafe_allow_html=True)