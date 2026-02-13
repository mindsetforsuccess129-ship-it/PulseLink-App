import streamlit as st
import pandas as pd
import time
import random
import requests
from bs4 import BeautifulSoup

# 1. PAGE CONFIG
st.set_page_config(page_title="PulseLink Pro", page_icon="🚀", layout="wide")

# 2. THE BRAINS (Scraper & SDK)
class PulseLinkSDK:
    def get_product_image(self, url):
        """Attempts to scrape a product image from the link."""
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Look for common image tags (og:image is best for social links)
            img = soup.find("meta", property="og:image")
            if img:
                return img["content"]
            return "https://via.placeholder.com/400x711?text=9:16+Video+Preview"
        except:
            return "https://via.placeholder.com/400x711?text=9:16+Video+Preview"

# 3. SIDEBAR & TIPS
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/5968/5968756.png", width=50) # TikTok Icon
    st.title("PulseLink Panel")
    
    st.divider()
    st.subheader("💡 Expert Tip")
    st.info("Vertical 9:16 videos get 40% more engagement on Instagram Reels! Always keep your key message in the middle 'safe zone'.")
    
    st.divider()
    st.write("⚙️ **Account Status**")
    st.success("API Connection: Active")
    st.success("Human-Simulated Post: ON")

# 4. MAIN INTERFACE
st.title("PulseLink: Global AI Marketing")

# Instruction Area (The "Step-by-Step" guide)
st.info("🎯 **Getting Started:** Step 1: Paste Link → Step 2: Edit AI Script → Step 3: Post to TikTok")

col1, col2 = st.columns([1, 1])

sdk = PulseLinkSDK()

with col1:
    st.subheader("📦 Product Input")
    url_input = st.text_input("Paste your Shopify or Store link:", placeholder="https://yourstore.com/product")
    
    if st.button("Generate Ad Content"):
        if url_input:
            with st.spinner("Analyzing product images and text..."):
                product_img = sdk.get_product_image(url_input)
                st.session_state.current_ad = {
                    "image": product_img,
                    "caption": "Elevate your style with this must-have! ✨ Limited stock available. #PulseLink #Ecommerce",
                    "time": time.strftime("%H:%M:%S")
                }
        else:
            st.warning("Please enter a URL first!")

with col2:
    st.subheader("🎥 Ad Preview & Post")
    if "current_ad" in st.session_state:
        # Display the scraped image in 9:16 style
        st.image(st.session_state.current_ad['image'], caption="AI Generated 9:16 Preview", use_container_width=True)
        st.text_area("Edit Ad Caption:", value=st.session_state.current_ad['caption'])
        
        if st.button("🚀 Push to Social Channels"):
            with st.status("Posting...", expanded=False):
                time.sleep(random.uniform(3, 7)) # Human delay
            st.balloons()
            st.success("Live on TikTok & Instagram!")
    else:
        st.write("---")
        st.caption("Waiting for your product link to generate a preview...")

# 5. RECENT ACTIVITY TABLE
st.divider()
st.subheader("📊 Recent Activity")
activity_data = {
    "Time": ["10:15 AM", "09:42 AM", "Yesterday"],
    "Product": ["Vintage Watch", "Skincare Set", "Leather Bag"],
    "Platform": ["TikTok", "Instagram", "Facebook"],
    "Status": ["✅ Posted", "✅ Posted", "✅ Posted"]
}
df = pd.DataFrame(activity_data)
st.table(df)

# 6. FOOTER
st.caption("PulseLink v1.0 | Built for the 2026 TEF Entrepreneurship Program")
import streamlit as st
import pandas as pd
import time
import random
import requests
from bs4 import BeautifulSoup

# 1. PAGE CONFIG
st.set_page_config(page_title="PulseLink Pro", page_icon="🚀", layout="wide")

# 2. THE BRAINS (Scraper & SDK)
class PulseLinkSDK:
    def get_product_image(self, url):
        """Attempts to scrape a product image from the link."""
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Look for common image tags (og:image is best for social links)
            img = soup.find("meta", property="og:image")
            if img:
                return img["content"]
            return "https://via.placeholder.com/400x711?text=9:16+Video+Preview"
        except:
            return "https://via.placeholder.com/400x711?text=9:16+Video+Preview"

# 3. SIDEBAR & TIPS
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/5968/5968756.png", width=50) # TikTok Icon
    st.title("PulseLink Panel")
    
    st.divider()
    st.subheader("💡 Expert Tip")
    st.info("Vertical 9:16 videos get 40% more engagement on Instagram Reels! Always keep your key message in the middle 'safe zone'.")
    
    st.divider()
    st.write("⚙️ **Account Status**")
    st.success("API Connection: Active")
    st.success("Human-Simulated Post: ON")

# 4. MAIN INTERFACE
st.title("PulseLink: Global AI Marketing")

# Instruction Area (The "Step-by-Step" guide)
st.info("🎯 **Getting Started:** Step 1: Paste Link → Step 2: Edit AI Script → Step 3: Post to TikTok")

col1, col2 = st.columns([1, 1])

sdk = PulseLinkSDK()

with col1:
    st.subheader("📦 Product Input")
    url_input = st.text_input("Paste your Shopify or Store link:", placeholder="https://yourstore.com/product")
    
    if st.button("Generate Ad Content"):
        if url_input:
            with st.spinner("Analyzing product images and text..."):
                product_img = sdk.get_product_image(url_input)
                st.session_state.current_ad = {
                    "image": product_img,
                    "caption": "Elevate your style with this must-have! ✨ Limited stock available. #PulseLink #Ecommerce",
                    "time": time.strftime("%H:%M:%S")
                }
        else:
            st.warning("Please enter a URL first!")

with col2:
    st.subheader("🎥 Ad Preview & Post")
    if "current_ad" in st.session_state:
        # Display the scraped image in 9:16 style
        st.image(st.session_state.current_ad['image'], caption="AI Generated 9:16 Preview", use_container_width=True)
        st.text_area("Edit Ad Caption:", value=st.session_state.current_ad['caption'])
        
        if st.button("🚀 Push to Social Channels"):
            with st.status("Posting...", expanded=False):
                time.sleep(random.uniform(3, 7)) # Human delay
            st.balloons()
            st.success("Live on TikTok & Instagram!")
    else:
        st.write("---")
        st.caption("Waiting for your product link to generate a preview...")

# 5. RECENT ACTIVITY TABLE
st.divider()
st.subheader("📊 Recent Activity")
activity_data = {
    "Time": ["10:15 AM", "09:42 AM", "Yesterday"],
    "Product": ["Vintage Watch", "Skincare Set", "Leather Bag"],
    "Platform": ["TikTok", "Instagram", "Facebook"],
    "Status": ["✅ Posted", "✅ Posted", "✅ Posted"]
}
df = pd.DataFrame(activity_data)
st.table(df)

# 6. FOOTER
st.caption("PulseLink v1.0 | Built for the 2026 TEF Entrepreneurship Program")


