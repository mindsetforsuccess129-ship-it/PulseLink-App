import streamlit as st
import pandas as pd
import time
import random
import requests
from bs4 import BeautifulSoup

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="PulseLink Pro", page_icon="🚀", layout="wide")

# 2. THE BRAINS (Scraper & SDK)
class PulseLinkSDK:
    def get_product_data(self, url):
        """Scrapes product image and the page title for the caption."""
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
            response = requests.get(url, headers=headers, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find Image (Look for OpenGraph image first)
            img_tag = soup.find("meta", property="og:image")
            img_url = img_tag["content"] if img_tag else "https://via.placeholder.com/400x711?text=9:16+Video+Preview"
            
            # Find Product Name from Page Title
            title_tag = soup.find("title")
            raw_title = title_tag.string.split('|')[0].split('-')[0].strip() if title_tag else "this amazing item"
            
            return {"image": img_url, "title": raw_title}
        except:
            return {"image": "https://via.placeholder.com/400x711?text=9:16+Video+Preview", "title": "this product"}

# 3. SIDEBAR (Marketing Icon & Settings)
with st.sidebar:
    # Growth Marketing Icon
    st.image("https://cdn-icons-png.flaticon.com/512/1998/1998087.png", width=80) 
    st.title("PulseLink Panel")
    
    st.divider()
    st.subheader("🎬 Video Settings")
    video_style = st.selectbox("Select Video Style:", ["Cinematic", "Hype/Fast-Paced", "Minimalist/Clean"])
    
    st.divider()
    st.write("⚙️ **System Status**")
    st.success("AI Engine: Active")
    st.success("Scraper: Ready")
    
    st.divider()
    st.info("💡 **Expert Tip:** Videos with captions get 80% more 'Sound-Off' views on TikTok!")

# 4. MAIN INTERFACE
st.title("PulseLink: Global AI Marketing")
st.info("🎯 **Workflow:** 1. Paste Link → 2. Select Style → 3. Post to TikTok")

col1, col2 = st.columns([1, 1])
sdk = PulseLinkSDK()

with col1:
    st.subheader("📦 Product Input")
    url_input = st.text_input("Paste product link:", placeholder="https://yourstore.com/product")
    
    if st.button("Generate Ad Content"):
        if url_input:
            with st.spinner("AI is analyzing product details..."):
                data = sdk.get_product_data(url_input)
                
                # Dynamic Caption Logic based on Video Style
                if "Hype" in video_style:
                    caption = f"🚨 BIG NEWS! The {data['title']} is finally here! 🚨 Don't sleep on this. Shop link in bio! ⚡️ #Viral #MustHave #PulseLink"
                elif "Minimalist" in video_style:
                    caption = f"The {data['title']}. \n\nSimple. Elegant. Yours. ✨ \n\n#MinimalStyle #Quality #PulseLink"
                else:
                    caption = f"Experience the new {data['title']}. \n\nElevate your daily routine with PulseLink AI. 🎬 \n\n#Cinematic #Innovation #PulseLink"
                
                st.session_state.current_ad = {
                    "image": data['image'],
                    "caption": caption,
                    "title": data['title']
                }
        else:
            st.warning("Please enter a URL first!")

with col2:
    st.subheader("🎥 9:16 Ad Preview")
    if "current_ad" in st.session_state:
        # Display the image in a 9:16-like container
        st.image(st.session_state.current_ad['image'], use_container_width=True)
        
        # Editable Caption Area
        st.session_state.current_ad['caption'] = st.text_area("Edit AI Script:", value=st.session_state.current_ad['caption'], height=150)
        
        if st.button("🚀 Push to Social Channels"):
            with st.status("Simulating Human Posting...", expanded=False):
                time.sleep(random.uniform(3, 6))
            st.balloons()
            st.success(f"Successfully posted to TikTok in '{video_style}' style!")
    else:
        st.write("---")
        st.caption("Enter a product link and click 'Generate' to see your AI-powered ad preview here.")

# 5. RECENT ACTIVITY TABLE
st.divider()
st.subheader("📊 Recent Activity")
activity_df = pd.DataFrame({
    "Time": ["Just now", "10:15 AM", "Yesterday"],
    "Product": [st.session_state.get('current_ad', {'title': '---'})['title'], "Vintage Watch", "Skincare Set"],
    "Platform": ["TikTok", "Instagram", "TikTok"],
    "Status": ["✅ Ready", "✅ Posted", "✅ Posted"]
})
st.table(activity_df)

# 6. FOOTER
st.caption("PulseLink Pro v1.1 | Built for the 2026 TEF Entrepreneurship Program")



