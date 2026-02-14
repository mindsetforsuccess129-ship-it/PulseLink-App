import streamlit as st
import pandas as pd
import time
import random
import requests

# 1. THE SAFETY CHECK (Keep this at the top)
try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False

# 2. PAGE CONFIG
st.set_page_config(page_title="PulseLink Pro", page_icon="🚀", layout="wide")

# 3. THE SCRAPER BRAIN
class PulseLinkSDK:
    def get_product_data(self, url):
        # This skips the scraper and gives you an instant result for the demo
        return {
            "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=1000", 
            "title": "Premium Pulse-Tech Watch"
        }


# 4. SIDEBAR (One instance only!)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1998/1998087.png", width=80) 
    st.title("PulseLink Panel")
    st.divider()
    
    st.subheader("🎬 Video Settings")
    # This is the only selectbox we need
    video_style = st.selectbox("Select Video Style:", ["Cinematic", "Hype/Fast-Paced", "Minimalist/Clean"], key="sidebar_style")
    
    st.divider()
    st.subheader("💰 Revenue Estimator")
    views = st.slider("Expected Views:", 1000, 100000, 5000, 1000)
    est_rev = (views * 0.02) * 25.0
    st.metric(label="Potential Revenue", value=f"${est_rev:,.2f}")
    
    st.divider()
    if HAS_BS4:
        st.success("✅ Scraper: Active")
    else:
        st.warning("⏳ Scraper: Initializing...")

# 5. MAIN INTERFACE
st.title("PulseLink: Global AI Marketing")
sdk = PulseLinkSDK()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📦 Product Input")
    url_input = st.text_input("Paste product link:", placeholder="https://yourstore.com/product")
    
    if st.button("Generate Ad Content"):
        if url_input:
            with st.spinner("AI analyzing link..."):
                data = sdk.get_product_data(url_input)
                cap = f"🚨 New Drop: {data['title']}! ✨ #Viral #PulseLink"
                st.session_state.current_ad = {"image": data['image'], "caption": cap, "title": data['title']}
        else:
            st.warning("Please enter a URL!")

with col2:
    st.subheader("🎥 9:16 Ad Preview")
                with st.spinner("AI analyzing link..."):
                data = sdk.get_product_data(url_input)
                # Ensure this next line starts exactly under 'data'
                cap = f"--- PULSELINK SCRIPT ---\nPRODUCT: {data['title']}\nSTYLE: {video_style}\n\nHOOK: 🚨 New Drop!\nBODY: The {data['title']} is a game changer. ✨\nCTA: Link in bio!\n\n#PulseLink #Viral"
                st.session_state.current_ad = {"image": data['image'], "caption": cap, "title": data['title']}


# 6. ACTIVITY
st.divider()
st.subheader("📊 Recent Activity")
st.table(pd.DataFrame({
    "Time": ["Just now", "10:15 AM"],
    "Product": [st.session_state.get('current_ad', {'title': '---'})['title'], "Vintage Watch"],
    "Status": ["✅ Ready", "✅ Posted"]
}))
