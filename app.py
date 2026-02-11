 
import streamlit as st

# Set page config for the "Cream" background feel
st.set_page_config(page_title="PulseLink Prototype", layout="centered")

# Custom CSS for the Blue and Cream look
st.markdown("""
    <style>
    .stApp { background-color: #FFFDD0; }
    .stButton>button { 
        background-color: #007BFF; 
        color: white; 
        border-radius: 8px; 
        width: 100%;
        height: 3em;
    }
    h1 { color: #003366; }
    </style>
    """, unsafe_allow_name=True)

st.title("🔗 PulseLink")
st.subheader("AI Automation for Global Dropshippers")

st.write("---")

# Main Interface
url_input = st.text_input("Paste your Shopify Product Link here:", "https://yourstore.com/product")

col1, col2 = st.columns(2)

with col1:
    if st.button("Generate TikTok Script"):
        st.success("Analyzing product details... Script generated!")

with col2:
    if st.button("Create Viral Video"):
        st.info("Video engine starting... Check back in 60 seconds.")

st.write("---")
st.caption("PulseLink Prototype v1.0 | Built for TEF 2026")
