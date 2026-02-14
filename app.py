import streamlit as st
import pandas as pd
import time
import random
import requests
from bs4 import BeautifulSoup

# 1. PAGE CONFIG
st.set_page_config(page_title="PulseLink Pro", page_icon="🚀", layout="wide")

# 2. THE SCRAPER BRAIN
class PulseLinkSDK:
    def get_product_data(self, url):
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            img_tag = soup.find("meta", property="og:image")
            img_url = img_tag["content"] if img_tag else "https://via.placeholder.com/400x711?text=Ad+Preview+Ready"
            title_tag = soup.find("title")
            raw_title = title_tag.string.split('|')[0].strip() if title_tag else "New Product"
            return {"image": img_url, "title": raw_title}
        except:
            return {"image": "https://via.placeholder.com/400x711?text=Ad+Preview+Ready", "title": "Product"}

# 3. SIDEBAR (Only ONE Revenue Estimator here)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1998/1998087.png", width=80) 
    st.title("PulseLink Panel")
    st.success("✅ System: Online")
    
    st.divider()
    st.subheader("💰 Revenue Estimator")
    # This is the only slider
    views = st.slider("Expected Views:", 1000, 100000, 5000, 1000, key="rev_slider")
    est_rev = (views * 0.01) * 5.0 
    st.metric(label="Potential Revenue", value=f"${est_rev:,.2f}")
    st.caption("Est. 1% conversion @ $5 commission")

# 4. MAIN INTERFACE
st.title("PulseLink: AI Ad Engine")
sdk = PulseLinkSDK()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📦 Product Input")
    url_input = st.text_input("Paste product link:", placeholder="https://example.com/item")
    
    if st.button("Generate Ad Content", key="gen_btn"):
        if url_input:
            with st.spinner("AI analyzing link..."):
                data = sdk.get_product_data(url_input)
                cap = f"🚨 New Drop: {data['title']}! ✨ Get yours now. #Viral #PulseLink"
                st.session_state.current_ad = {"image": data['image'], "caption": cap, "title": data['title']}
        else:
            st.warning("Please enter a URL!")

with col2:
    st.subheader("🎥 9:16 Ad Preview")
    if "current_ad" in st.session_state:
        st.image(st.session_state.current_ad['image'], use_container_width=True)
        final_cap = st.text_area("AI Script:", value=st.session_state.current_ad['caption'], height=100)
        
        # Action Buttons
        c1, c2 = st.columns(2)
        with c1:
            if st.button("🚀 Push to Social"):
                st.balloons()
        with c2:
            st.download_button("📥 Download Script", data=final_cap, file_name="PulseLink_Script.txt")
    else:
        st.info("Your ad preview will appear here after you click 'Generate'.")

