import streamlit as st
from streamlit_image_comparison import image_comparison

# set page config
st.set_page_config(page_title="Image-Comparison Example", layout="centered")

# render image-comparison
aa=image_comparison(
    img1="http://yun.sfo2.digitaloceanspaces.com/t/streamlit0.png",
    img2="http://yun.sfo2.digitaloceanspaces.com/t/streamlit1.png",
    
)

