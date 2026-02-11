
import streamlit as st

# Page setup
st.set_page_config(page_title="PulseLink Prototype", layout="centered")

# Final UI Polish
st.markdown("""
    <style>
    .stApp { background-color: #FFFDD0; } /* Cream Background */
    
    /* Dark Navy for all main text */
    h1, h2, h3, p, span, label { 
        color: #002147 !important; 
        font-weight: bold;
    }
    
    /* Professional Blue Buttons */
    .stButton>button { 
        background-color: #007BFF; 
        color: white !important; 
        border-radius: 8px; 
        border: none;
    }
    
    /* FIX: Make the link text white and easy to read */
    input { 
        color: white !important; 
        background-color: #262730 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔗 PulseLink")
st.subheader("AI Automation for Global Dropshippers")

st.write("---")

st.info("Prototype Demo: Paste a link below to see the automation bridge in action.")

# The input box where the link will now be bright and clear
url_input = st.text_input("Paste Shopify Product Link:", "https://yourstore.com/product")

if st.button("🚀 Generate TikTok Script"):
    st.success("Analysis Complete: Script optimized for high-conversion!")

if st.button("🎬 Create Viral Video"):
    st.warning("Video Rendering Engine: Initializing preview...")

st.write("---")
st.caption("PulseLink v1.0 | Developed by Esther David for TEF 2026")
