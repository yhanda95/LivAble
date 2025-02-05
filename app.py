import streamlit as st
import base64
import os
from predict_page import load_data

def get_base64_of_bin_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(file_path):
    try:
        bin_str = get_base64_of_bin_file(file_path)
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error loading background image: {str(e)}")

def load_custom_css():
    # Get the path to your background image
    image_path = os.path.join(os.path.dirname(__file__), 'static', 'background.jpg')
    
    # Set the background
    set_background(image_path)
    
    # Rest of the custom CSS
    st.markdown("""
    <style>
    .stButton>button {
        background-color: rgb(18, 173, 106) !important;
        color: white !important;
    }
    
    .about-section {
        background-color: rgba(255, 255, 255, 0.38);
        backdrop-filter: blur(1px);
        border-radius: 10px;
        padding: 15px;
        margin-top: 40px;
    }

    /* Center the PowerBI dashboard */
    .dashboard-container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        margin: 0 auto;
    }

    iframe {
        margin: 0 auto;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

def landing_page():
    st.title("Welcome to the Livability Analysis App")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🔍 Analyze", key="analyze_button", use_container_width=True):
            st.session_state['page']="Analyze"

    with col2:
        if st.button("📈 Predict", key="predict_button", use_container_width=True):
            st.session_state['page'] = "Predict"

    st.markdown(
        """
        <div class="about-section">
            <h4>About the Project</h4>
            <p>
            This app provides tools to analyze and predict livability factors for countries worldwide.<br>
            <strong>Analyze:</strong> Dive into detailed visual insights with our integrated PowerBI dashboard.<br>
            <strong>Predict:</strong> Explore and compare rankings for health, education, and more.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

def analyze_page():
    st.title("Livability Analysis Dashboard")
    st.markdown("""
    <div class="dashboard-container">
        <iframe title="report_mini_project" width="900" height="550" src="https://app.powerbi.com/reportEmbed?reportId=47b2c1af-0d91-4115-a159-112f1a4a1fca&autoAuth=true&ctid=29d6b2c1-5a07-49dc-ad3b-a84fe545e6d9" frameborder="0" allowFullScreen="true"></iframe>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("⬅️ Go Back to Landing Page", key="go_back_analyze"):
        st.session_state['page'] = "Landing"

def predict_page():
    load_data()
    
    if st.button("⬅️ Go Back to Landing Page", key="go_back_predict"):
        st.session_state['page'] = "Landing"

def main():
    load_custom_css()

    if 'page' not in st.session_state:
        st.session_state['page'] = "Landing"

    if st.session_state['page'] == "Landing":
        landing_page()
    elif st.session_state['page'] == "Analyze":
        analyze_page()
    elif st.session_state['page'] == "Predict":
        predict_page()

main()
