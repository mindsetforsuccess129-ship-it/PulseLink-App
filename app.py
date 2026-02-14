import streamlit as st  # Updated
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
        if not HAS_BS4:
            return {"image": "https://via.placeholder.com/400x711?text=System+Updating...", "title": "Product"}
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            img_tag = soup.find("meta", property="og:image")
            img_url = img_tag["content"] if img_tag else "https://via.placeholder.com/400x711?text=9:16+Preview"
            title_tag = soup.find("title")
            raw_title = title_tag.string.split('|')[0].strip() if title_tag else "this item"
            return {"image": img_url, "title": raw_title}
        except:
            return {"image": "https://via.placeholder.com/400x711?text=9:16+Preview", "title": "product"}

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
    if "current_ad" in st.session_state:
        st.image(st.session_state.current_ad['image'], use_container_width=True)
        final_cap = st.text_area("AI Script:", value=st.session_state.current_ad['caption'], height=100)
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("🚀 Push to Social"):
                st.balloons()
        with c2:
            st.download_button("📥 Download", data=final_cap, file_name="script.txt")
    else:
        st.caption("Enter a link to see preview...")

# 6. ACTIVITY
st.divider()
st.subheader("📊 Recent Activity")
st.table(pd.DataFrame({
    "Time": ["Just now", "10:15 AM"],
    "Product": [st.session_state.get('current_ad', {'title': '---'})['title'], "Vintage Watch"],
    "Status": ["✅ Ready", "✅ Posted"]
}))
# Force Refresh
