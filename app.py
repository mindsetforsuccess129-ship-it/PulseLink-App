import streamlit as st

# Page setup
st.set_page_config(page_title="PulseLink Prototype", layout="centered")

# Corrected CSS for the Blue and Cream look
st.markdown("""
    <style>
    .stApp { background-color: #FFFDD0; }
    .stButton>button { 
        background-color: #007BFF; 
        color: white; 
        border-radius: 8px; 
        width: 100%;
    }
    h1 { color: #003366; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔗 PulseLink")
st.subheader("AI Automation for Global Dropshippers")

st.write("---")
url_input = st.text_input("Paste Shopify Link:", "https://yourstore.com/product")

if st.button("Generate TikTok Script"):
    st.success("Script generated successfully!")

if st.button("Create Viral Video"):
    st.info("Video engine starting...")
