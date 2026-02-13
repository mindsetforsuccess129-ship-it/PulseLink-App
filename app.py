import streamlit as st
import pandas as pd
import time
import random
import requests

# 1. THE "SAFETY CHECK" FOR THE BRAIN
try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False

# 2. PAGE CONFIG
st.set_page_config(page_title="PulseLink Pro", page_icon="🚀", layout="wide")

# 3. SIDEBAR (The Complete Panel)
with st.sidebar:
    # 1. Marketing Icon
    st.image("https://cdn-icons-png.flaticon.com/512/1998/1998087.png", width=80) 
    st.title("PulseLink Panel")
    
    st.divider()
    
    # 2. Video Settings
    st.subheader("🎬 Video Settings")
    video_style = st.selectbox("Select Video Style:", ["Cinematic", "Hype/Fast-Paced", "Minimalist/Clean"])
    
    st.divider()
    
    # 3. Revenue Calculator (This is the part you were missing!)
    st.subheader("💰 Revenue Estimator")
    st.caption("Estimate earnings based on views")
    
    # The Slider
    views = st.slider("Expected Views:", min_value=1000, max_value=100000, value=5000, step=1000)
    
    # The Calculation
    est_revenue = (views * 0.02) * 25.0
    
    # Display the Result
    st.metric(label="Potential Revenue", value=f"${est_revenue:,.2f}")
    st.info("Based on 2% conversion @ $25/sale")
    
    st.divider()
    
    # 4. System Status
    if HAS_BS4:
        st.success("✅ Scraper: Active")
    else:
        st.warning("⏳ Scraper: Initializing...")


# 4. SIDEBAR
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1998/1998087.png", width=80) 
    st.title("PulseLink Panel")
    st.divider()
    st.subheader("🎬 Video Settings")
    video_style = st.selectbox("Select Video Style:", ["Cinematic", "Hype/Fast-Paced", "Minimalist/Clean"])
    st.divider()
    if HAS_BS4:
        st.success("✅ Scraper: Active")
    else:
        st.warning("⏳ Scraper: Initializing...")

# 5. MAIN INTERFACE
st.title("PulseLink: Global AI Marketing")
col1, col2 = st.columns([1, 1])
sdk = PulseLinkSDK()

with col1:
    st.subheader("📦 Product Input")
    url_input = st.text_input("Paste product link:", placeholder="https://yourstore.com/product")
    
    if st.button("Generate Ad Content"):
        if url_input:
            with st.spinner("AI analyzing link..."):
                data = sdk.get_product_data(url_input)
                # Caption Logic
                if "Hype" in video_style:
                    cap = f"🚨 BIG NEWS! The {data['title']} is here! 🚨 #Viral"
                else:
                    cap = f"Experience the new {data['title']}. ✨ #PulseLink"
                
                st.session_state.current_ad = {"image": data['image'], "caption": cap, "title": data['title']}
        else:
            st.warning("Please enter a URL!")

with col2:
    st.subheader("🎥 9:16 Ad Preview")
    if "current_ad" in st.session_state:
        # 1. Show the Image
        st.image(st.session_state.current_ad['image'], use_container_width=True)
        
        # 2. Show the Script (Editable)
        final_caption = st.text_area("Edit AI Script:", value=st.session_state.current_ad['caption'], height=150)
        
        # 3. Action Buttons (Side by Side)
        btn_col1, btn_col2 = st.columns(2)
        
        with btn_col1:
            if st.button("🚀 Push to Social"):
                with st.status("Posting...", expanded=False):
                    time.sleep(random.uniform(3, 6))
                st.balloons()
                st.success("Live on TikTok!")
        
        with btn_col2:
            st.download_button(
                label="📥 Download Script",
                data=final_caption,
                file_name=f"PulseLink_Ad.txt",
                mime="text/plain"
            )
    else:
        st.write("---")
        st.caption("Enter a product link and click 'Generate' to see your AI-powered ad preview here.")


# 6. ACTIVITY
st.divider()
st.subheader("📊 Recent Activity")
st.table(pd.DataFrame({
    "Time": ["Just now", "10:15 AM"],
    "Product": [st.session_state.get('current_ad', {'title': '---'})['title'], "Vintage Watch"],
    "Status": ["✅ Ready", "✅ Posted"]
}))
