import streamlit as st
from pages import information, preprocessing, home

pages = {
    "Information about the dataset": information,
    "Preprocessing": preprocessing,
    "Home": home
}

# import streamlit as st

# # Set the page layout (optional)
# st.set_page_config(layout="wide")

# # Custom CSS to remove all default UI elements
# hide_streamlit_default_elements = """
#     <style>
#         #MainMenu {visibility: hidden;} /* Hides the hamburger menu */
#         footer {visibility: hidden;}   /* Hides the footer */
#         header {visibility: hidden;}   /* Hides the header */
#         [data-testid="collapsedControl"] {display: none;} /* Hides the sidebar toggle button */
#     </style>
# """
# st.markdown(hide_streamlit_default_elements, unsafe_allow_html=True)

# # Your custom app content
# st.title("Custom Streamlit App")
# st.write("This app has no default Streamlit UI elements.")

# Custom sidebar navigation
# st.sidebar.title("Navigation")
# page_selection = st.sidebar.radio("Go to", list(pages.keys()))
# page = pages[page_selection]
# page.app()
