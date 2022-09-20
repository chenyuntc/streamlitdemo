import streamlit as st
from streamlit_image_comparison import image_comparison

# set page config
st.set_page_config(page_title="Image-Comparison Example", layout="centered")

# render image-comparison
aa=image_comparison(
    img1="/mnt2/remote/shared_data/users/yun/logs/p/gan_instance/053/015000_res2.png",
    img2="/mnt2/remote/shared_data/users/yun/logs/p/gan_basic/053/015000_res2.png",
    
)

