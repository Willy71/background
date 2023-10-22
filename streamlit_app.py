import streamlit as st
import requests
from PIL import Image
import base64

# Colocar nome na pagina, icone e ampliar a tela
st.set_page_config(
    page_title="Guillermo Cerato",
    page_icon="💻",
    layout="wide"
)

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

coding = Image.open('python.png')
uber_ny = Image.open('uber_ny.jpg')
cyclist = Image.open('Cyclist_sc.jpg')
streamlit = Image.open('streamlit_logo.jpg')
coding_small = 'coding_small.gif'

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown(
    f'<div style="display: flex; justify-content: center;">'
    f'<img src="https://i.postimg.cc/BnNQFd7x/nombre.png" width="800">'
    f'</div>',
    unsafe_allow_html=True
)
st.markdown("<h1 style='text-align:center; color: white'>Data analyst</h1>", unsafe_allow_html=True)
st.markdown(
    f'<div style="display: flex; justify-content: center;">'
    f'<img src="https://i.postimg.cc/yYdfB94s/willy-002.png" width="300">'
    f'</div>',
    unsafe_allow_html=True
)

st.markdown("<h3 style='text-align: center; color: white'>Portfolio on data analysis, web page creation and machine learning, based on Python</h3>", unsafe_allow_html=True)
     

with st.container():
    st.write("---")
    col6, col7 = st.columns(2)
    with col6:
        st.markdown("<h1 style='text-align: center; color: white'>My objective</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: white'>Welcome to my website, which focuses on showcasing my work. The goal is for them to be able to evaluate my performance and skills. Python, SQL, Excel, Power BI, Streamlit will be the most used in my work.</h4>", unsafe_allow_html=True)
        #st.write(
            #"[Work done with Streamlit >](https://uberviajes.streamlit.app/)")
    with col7:
        col8, col9, col10 = st.columns([4, 8, 4])
        with col9:
            st.text(" ")
            st.text(" ")
            st.text(" ")
            st.image(coding_small, width=280, use_column_width=True)

st.write("---")
st.markdown("<h1 style='text-align: center; color: white'>Works</h1>", unsafe_allow_html=True)

with st.container():    
    col50, col51, col53 = st.columns(3)
    with col50:
        st.image(uber_ny, width=300)
        with st.container():
            col54, col55, col56 = st.columns([2.5,5,3])
            with col55:
                st.write("[Uber - New York](https://uberviajes.streamlit.app/)")
    with col51:
        st.image(cyclist, width=300)
        with st.container():
            col57, col58, col59 = st.columns([2,5,3])
            with col58:
                st.write("[Study Case - Cyclist](https://www.kaggle.com/code/willycerato/case-study-cyclistic-python)") 

with st.container():
    st.write("---")
    col11, col12 = st.columns(2)
    with col11:
        st.markdown("<h2 style='text-align: center; color: white'>Website made with Streamlit</h2>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: blue;'>Programmed with Python</h2>", unsafe_allow_html=True)
    with col12:
        col3, col14, col15, col16, col17 = st.columns(5)
        with col14:            
            st.text(" ")
            st.text(" ")
            st.markdown(
                f'<div style="display: flex; justify-content: center;">'
                f'<img src="https://i.postimg.cc/V6Jjp90V/streamlit-logo.jpg" width="150">'
                f'</div>',
                unsafe_allow_html=True
            )           
        with col16:
            st.markdown(
                f'<div style="display: flex; justify-content: center;">'
                f'<img src="https://i.postimg.cc/1znXZvMw/python.png" width="150">'
                f'</div>',
                unsafe_allow_html=True
            )              
st.write("---")
