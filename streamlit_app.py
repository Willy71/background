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

def photo_link(alt_text, img_url, link_url, img_width):
    markdown_code = f'<a href="{link_url}" target="_blank"><img src="{img_url}" alt="{alt_text}" width="{img_width}"></a>'
    st.markdown(markdown_code, unsafe_allow_html=True)

def centrar_imagen(imagen, ancho):
    # Aplicar estilo CSS para centrar la imagen con Markdown
    st.markdown(
        f'<div style="display: flex; justify-content: center;">'
        f'<img src="{imagen}" width="{ancho}">'
        f'</div>',
        unsafe_allow_html=True
    )

def centrar_imagen_link(imagen, link, nombre, ancho):
    st.markdown(
        f"""
        <style>
            .imagen-enlace {{
                cursor: pointer;
                transition: transform 0.3s;
            }}
        </style>
        <div style="display: flex; justify-content: center;">
            <a href="{imagen}" target="_blank">
                <img class="imagen-enlace" src="{imagen}" width="{ancho}" alt="{nombre}">
            </a>
        </div>
        <h5 style='text-align: center;'><a href='{link}' target="_blank">{nombre}</a></h5>
        """,
        unsafe_allow_html=True
    )

def centrar_texto(texto, tamanho, color):
    st.markdown(f"<h{tamanho} style='text-align: center; color: {color}'>{texto}</h{tamanho}>",
            unsafe_allow_html=True)

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.postimg.cc/J7Qkwt4s/pxfuel-1.jpg");
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

st.write("#")

st.markdown(
    f'<div style="display: flex; justify-content: center;">'
    f'<img src="https://i.postimg.cc/ZnZ99gWf/Encabezado-nombre-removebg-preview.png" width="320">'
    f'</div>',
    unsafe_allow_html=True
)
#st.markdown("<h1 style='text-align:center; color: white'>Data analyst</h1>", unsafe_allow_html=True)
st.markdown(
    f'<div style="display: flex; justify-content: center;">'
    f'<img src="https://i.postimg.cc/ry1CPRMy/willy-004.png" width="300">'
    f'</div>',
    unsafe_allow_html=True
)

st.markdown("<h3 style='text-align: center; color: white'>Data analyst and Python programmer</h3>", unsafe_allow_html=True)

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

with st.container():
    col6, col7 = st.columns(2)
    with col6:
        #st.markdown("<h1 style='text-align: center; color: white'>Objective</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: white'>Welcome to my website, which focuses on showcasing my work. The goal is for them to be able to evaluate my performance and skills. Python, SQL, Excel, Power BI, Streamlit will be the most used in my work.</h4>", unsafe_allow_html=True)
        #st.write(
            #"[Work done with Streamlit >](https://uberviajes.streamlit.app/)")
    with col7:
        st.markdown(
            f'<div style="display: flex; justify-content: center;">'
            f'<img src="https://i.postimg.cc/TPvkg31s/programmer.jpg" width="300">'
            f'</div>',
            unsafe_allow_html=True
        )

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white'>Works</h1>", unsafe_allow_html=True)
st.text("")

with st.container():    
    col50, col51, col52, col53, col54 = st.columns(5)
    with col50:
        centrar_imagen_link("https://i.postimg.cc/3N2Ny1cV/Cyclist-sc.jpg", "https://i.postimg.cc/3N2Ny1cV/Cyclist-sc.jpg", "Study Case Coursera", 210)       
    with col51:
        centrar_imagen_link("https://i.postimg.cc/SNZBWggx/super001.jpg", 'https://github.com/Willy71/supermercados', "Supermarket", 200) 
    with col52:
        centrar_imagen_link("https://i.postimg.cc/nV2gJdbG/tareas001.jpg", 'https://github.com/Willy71/tareas',"Daily task manager", 210)
    with col53:
        centrar_imagen_link("https://i.postimg.cc/qqJFKKnK/lavajato.jpg", 'https://github.com/Willy71/washcar', "Washcar", 175)
    with col54:
        centrar_imagen_link("https://i.postimg.cc/K8wCWRSX/Estacionamiento.jpg", 'https://github.com/Willy71/parking', "Parking", 160)
        
    
with st.container():    
    col55, col56, col57, col58, col59 = st.columns(5)
    with col55:
        centrar_imagen_link("https://i.postimg.cc/qqrT5gKB/Hotel001.jpg", "https://hotelservice.streamlit.app/", "hotel", 205)     
    with col56:
        centrar_imagen_link("https://i.postimg.cc/wBwg9KZY/streamlit-page.jpg", 'https://github.com/Willy71/background/', "Web page with Python",200)    
    with col57:
        centrar_imagen_link("https://i.postimg.cc/wxZdC9Zf/uber-ny.jpg", "https://uberviajes.streamlit.app/", "Uber - New York", 220)
    with col58:
        centrar_imagen_link("https://i.postimg.cc/wTSwXgS5/preserntation.jpg", 'https://futbolargentino.streamlit.app', "Soccer Argentina", 215)
    with col59:
        centrar_imagen_link("https://i.postimg.cc/bv5pP5T8/fifa2023.jpg", 'https://jugadores2023.streamlit.app/', "Fifa 2023", 210)
      
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

centrar_texto("About me", 3, "white")

centrar_texto('Argentine resident in Brazil since 2016, I am a family man with a Brazilian wife, Samella, and two children,', 6, 'white')
centrar_texto('Benício Luca and Ester Valentina. Professionally I have diverse experiences, mainly in tourism as a', 6, 'white')
centrar_texto('micro-entrepreneur and running Lupita Hostel e Pousada in Maceió. Later I ventured into making and selling', 6, 'white')
centrar_texto('alfajores during and after the pandemic, displayed at @alfajor.milagros on Instagram.', 6, 'white')
st.title("#")
centrar_texto('My previous career in Argentina involved sales at Unifon, including managing their sales team,', 6, 'white') 
centrar_texto('and then at Parmalat as a supervisor. I joined Nokia in 2006 and worked as a field supervisor,', 6, 'white') 
centrar_texto('supervising a team, organizing events and participating in sales and commercial management.', 6, 'white')
st.title("#")
centrar_texto('Throughout my career, I have consistently worked with metrics, data, and statistical analysis,', 6, 'white') 
centrar_texto('primarily using Excel. My interest in data analysis led me to explore tools beyond Excel, such as SQL,', 6, 'white') 
centrar_texto('Python, and Power BI. I am a Python programmer, I enrolled in the Google Data Analytics PT by Coursera', 6, 'white') 
centrar_texto('course to further structure my studies. My innate curiosity and dedication drive me to continually learn', 6, 'white') 
centrar_texto('and hone my skills in the ever-evolving field of data analytics.', 6, 'white')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

centrar_texto("Academic training", 1, "white")
centrar_texto("Profissional Google Data Analytics by Coursera", 4, "white")
st.title("#")
with st.container():
    col201, col202, col203, col204 = st.columns([1,2,1,3])
    with col202:
        centrar_texto("Share data with the art of visualization", 7, "white")
        centrar_texto("Data analysis with R programming", 7, "white")
        centrar_texto("Analyze data to answer questions", 7, "white")
        centrar_texto("Fundamentals: Data, Data, Everywhere", 7, "white")
        centrar_texto("Process the data to clean it", 7, "white")
        centrar_texto("Prepare Data for Exploration", 7, "white")
        centrar_texto("Google Data Analytics Final Project: Complete a Case Study", 7, "white")
        centrar_texto("Ask questions to make data-driven decisions", 7, "white")
    with col204:
        centrar_imagen("https://i.postimg.cc/nrSXrRzC/Titulo-coursera.jpg", 350)
        st.markdown("[Title link](https://www.coursera.org/account/accomplishments/professional-cert/LMTDNASPE8WP)")

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
        
centrar_texto("Recommendations", 1, "white")
st.markdown("<h3 style='text-align:left; color: white'>Maximiliano Roca Saran - Key account manager - Mobile phones</h3>", unsafe_allow_html=True)
centrar_texto("Guillermo is an excellent manager, always predisposed, very focused on what he does and results-oriented. He is a very good team builder. He is always willing to learn new things and change.", 7, "white")

st.title("")
st.markdown("<h3 style='text-align:left; color: white'>Cristina Jacquemin - Accounts director - Grupo Solvens</h3>", unsafe_allow_html=True)
centrar_texto("Guillermo is without a doubt a great professional in his area, a great leader and generator of efficient work teams!", 7, "white")

st.title("")
st.markdown("<h3 style='text-align:left; color: white'>Ariel Smirnoff - Business coach</h3>", unsafe_allow_html=True) 
centrar_texto("Guillermo was always super considerate of his team, but also demanding, accompanying each one in their needs and developing personnel for which he worked in a structured way through action plans, which allowed him to check if the collaborator did not know (he taught them) ; if he couldn't (help him); but if he didn't want to there was no waste of time.Super results oriented. Reliable in customer service (retailers) and territory development, average ticket, arpu, ROI, market share, brand visibility, and retailer training. He always showed himself with professionalism, enthusiasm and speed, the team he led achieved results and expanded the area. Collaborators also emerged who were able to grow and develop under his direction.", 7, "white")

st.title("")
st.markdown("<h3 style='text-align:left; color: white'>Agustin Valdes Marteles - Make it happen</h3>", unsafe_allow_html=True)
centrar_texto("Excellent person and excellent professional. Very human and ideal for the position in which we share company. It has been a pleasure to work with him.", 7, "white")

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white'>Contact</h1>", unsafe_allow_html=True)
st.title("")

with st.container():    
    col50, col51, col52, col53, col54, col55, col56, col57 = st.columns(8)
    with col51:
        photo_link("Kaggle", "https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/189_Kaggle_logo_logos-512.png", "https://www.kaggle.com/willycerato", "50px")
    with col52:
        photo_link("Github", "https://cdn.pixabay.com/photo/2022/01/30/13/33/github-6980894_1280.png", "https://github.com/Willy71", "50px")
    with col53:
        photo_link("Instagram", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Instagram_logo_2022.svg/150px-Instagram_logo_2022.svg.png", "https://www.instagram.com/willycerato", "50px")
    with col54:
        photo_link("Facebook", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/2023_Facebook_icon.svg/50px-2023_Facebook_icon.svg.png", "https://www.facebook.com/guillermo.cerato", "50px")
    with col55:
        photo_link("Linkedin", "https://img.freepik.com/vetores-premium/logotipo-quadrado-do-linkedin-isolado-no-fundo-branco_469489-892.jpg", "https://www.linkedin.com/in/willycerato", "50px")        
    with col56:
        photo_link("Whatsapp", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/120px-WhatsApp.svg.png", "https://wa.me/5542991657847", "50px")

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

with st.container():
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
                f'<img src="https://i.postimg.cc/vTVs74BG/streamlit-logo.jpg" width="150">'
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
            
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

