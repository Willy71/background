import streamlit as st
import requests
from PIL import Image
import base64

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.postimg.cc/6pnkb8sw/back-dev.jpg");
background-size: 180%;
background-position: top left;
background-repeat: repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center; color: white'>Guillermo Cerato</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; color: white'>Data analyst</h2>", unsafe_allow_html=True)
