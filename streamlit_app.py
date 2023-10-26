import streamlit as st
import requests
from PIL import Image
import base64

# Colocar nome na pagina, icone e ampliar a tela
st.set_page_config(
    page_title="Portfolio - Guillermo Cerato",
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
st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown(
    f'<div style="display: flex; justify-content: center;">'
    f'<img src="https://i.postimg.cc/BnNQFd7x/nombre.png" width="600">'
    f'</div>',
    unsafe_allow_html=True
)
st.markdown("<h1 style='text-align:center; color: white'>Data analyst</h1>", unsafe_allow_html=True)
st.markdown(
    f'<div style="display: flex; justify-content: center;">'
    f'<img src="https://i.postimg.cc/ry1CPRMy/willy-004.png" width="300">'
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
        st.text("")
        st.text("")
        st.text("")
        st.markdown(
            f'<div style="display: flex; justify-content: center;">'
            f'<img src="https://i.postimg.cc/TPvkg31s/programmer.jpg" width="300">'
            f'</div>',
            unsafe_allow_html=True
        )

st.write("---")
st.markdown("<h1 style='text-align: center; color: white'>Works</h1>", unsafe_allow_html=True)

with st.container():    
    col50, col51, col52 = st.columns(3)
    with col50:
        st.markdown("<h3 style='text-align:center; color: white'>Uber - New York</h3>", unsafe_allow_html=True)
        st.markdown(
            f'<div style="display: flex; justify-content: center;">'
            f'<img src="https://i.postimg.cc/wxZdC9Zf/uber-ny.jpg" width="300">'
            f'</div>',
            unsafe_allow_html=True
        )
        st.markdown("<h5 style='text-align: center;'><a href='https://uberviajes.streamlit.app/'>Link</a></h5>", unsafe_allow_html=True)        
    with col51:
        st.markdown("<h3 style='text-align:center; color: white'>Study Case Coursera</h3>", unsafe_allow_html=True)
        st.markdown(
            f'<div style="display: flex; justify-content: center;">'
            f'<img src="https://i.postimg.cc/3N2Ny1cV/Cyclist-sc.jpg" width="300">'
            f'</div>',
            unsafe_allow_html=True
        )
        st.markdown("<h5 style='text-align: center;'><a href='https://www.kaggle.com/code/willycerato/case-study-cyclistic-python'>Link</a></h5>", unsafe_allow_html=True)
    with col52:
        st.markdown("<h3 style='text-align:center; color: white'>Web page with Python</h3>", unsafe_allow_html=True)
        st.markdown(
            f'<div style="display: flex; justify-content: center;">'
            f'<img src="https://i.postimg.cc/kgYJgL5D/streamlit-page.jpg" width="300">'
            f'</div>',
            unsafe_allow_html=True
        )
        st.markdown("<h5 style='text-align: center;'><a href='https://github.com/Willy71/background/'>Link</a></h5>", unsafe_allow_html=True)

with st.container():    
    col53, col54, col55 = st.columns(3)
    with col53:
        st.markdown("<h3 style='text-align:center; color: white'>Fifa 2023</h3>", unsafe_allow_html=True)
        st.markdown(
            f'<div style="display: flex; justify-content: center;">'
            f'<img src="https://i.postimg.cc/bv5pP5T8/fifa2023.jpg" width="300">'
            f'</div>',
            unsafe_allow_html=True
        )
        st.markdown("<h5 style='text-align: center;'><a href='https://jugadores2023.streamlit.app/'>Link</a></h5>", unsafe_allow_html=True) 




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

st.markdown('![Visitor count](https://shields-io-visitor-counter.herokuapp.com/badge?page=https://share.streamlit.io/your_deployed_app_link&label=VisitorsCount&labelColor=000000&logo=GitHub&logoColor=FFFFFF&color=1D70B8&style=for-the-badge)')
