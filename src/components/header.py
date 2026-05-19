import streamlit as st
import base64
import os

# Helper function to convert local image to base64
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    except Exception as e:
        st.error(f"Could not load image. Error: {e}")
        return None

def header_home():
    # 1. This gets you to: .../src/components
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Go UP two levels to reach the root folder: .../AUTH_ECHO_VOX
    root_dir = os.path.dirname(os.path.dirname(current_dir))
    
    # 3. Now look for assets/logo.png from the root!
    logo_path = os.path.join(root_dir, "assets", "logo.png")
    
    img_base64 = get_base64_image(logo_path)
    
    if img_base64:
        st.markdown(f"""
            <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
                <img src="data:image/png;base64,{img_base64}" style="height:100px;" />
                <h1 style='text-align:center; color:#E0E3FF'>AUTH VISION <br> VOX</h1>
            </div>   
        """, unsafe_allow_html=True)

def header_dashboard():
    # Apply the same logic here!
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(os.path.dirname(current_dir)) # Go up two levels
    logo_path = os.path.join(root_dir, "assets", "logo.png")
    
    img_base64 = get_base64_image(logo_path)
    
    if img_base64:
        st.markdown(f"""
            <div style="display:flex; align-items:center; justify-content:center; gap:10px">
                <img src="data:image/png;base64,{img_base64}" style="height:85px;" />
                <h2 style='text-align:left; color:#5865F2'>AUTH VISION <br> VOX</h2>
            </div>   
        """, unsafe_allow_html=True)