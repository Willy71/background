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

def centrar_imagen(imagen, ancho):
    # Aplicar estilo CSS para centrar la imagen con Markdown
    st.markdown(
        f'<div style="display: flex; justify-content: center;">'
        f'<img src="{imagen}" width="{ancho}">'
        f'</div>',
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

def photo_link(alt_text, img_url, link_url, img_width):
    markdown_code = f'<a href="{link_url}" target="_blank"><img src="{img_url}" alt="{alt_text}" width="{img_width}"></a>'
    st.markdown(markdown_code, unsafe_allow_html=True)

st.write("#")

st.markdown(
    f'<div style="display: flex; justify-content: center;">'
    f'<img src="https://i.postimg.cc/ZnZ99gWf/Encabezado-nombre-removebg-preview.png" width="320">'
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

st.markdown("<h3 style='text-align: center; color: white'>Portfolio on data analysis based on Python</h3>", unsafe_allow_html=True)

st.write("-")

with st.container():
    st.write("---")
    col6, col7 = st.columns(2)
    with col6:
        st.markdown("<h1 style='text-align: center; color: white'>Objective</h1>", unsafe_allow_html=True)
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
    col50, col51, col52, col53, col54 = st.columns(5)
    with col51:
        st.markdown("<h5 style='text-align:center; color: white'>Uber - New York</h5>", unsafe_allow_html=True)
        st.markdown(
            f'<div style="display: flex; justify-content: center;">'
            f'<img src="https://i.postimg.cc/wxZdC9Zf/uber-ny.jpg" width="200">'
            f'</div>',
            unsafe_allow_html=True
        )
        st.markdown("<h5 style='text-align: center;'><a href='https://uberviajes.streamlit.app/'>Link</a></h5>", unsafe_allow_html=True)        
    with col52:
        st.markdown("<h5 style='text-align:center; color: white'>Study Case Coursera</h5>", unsafe_allow_html=True)
        st.markdown(
            f'<div style="display: flex; justify-content: center;">'
            f'<img src="https://i.postimg.cc/3N2Ny1cV/Cyclist-sc.jpg" width="200">'
            f'</div>',
            unsafe_allow_html=True
        )
        st.markdown("<h5 style='text-align: center;'><a href='https://www.kaggle.com/code/willycerato/case-study-cyclistic-python'>Link</a></h5>", unsafe_allow_html=True)
    with col53:
        st.markdown("<h5 style='text-align:center; color: white'>Web page with Python</h5>", unsafe_allow_html=True)
        st.markdown(
            f'<div style="display: flex; justify-content: center;">'
            f'<img src="https://i.postimg.cc/wBwg9KZY/streamlit-page.jpg" width="200">'
            f'</div>',
            unsafe_allow_html=True
        )
        st.markdown("<h5 style='text-align: center;'><a href='https://github.com/Willy71/background/'>Link</a></h5>", unsafe_allow_html=True)
    
with st.container():    
    col55, col56, col57, col58 = st.columns(4)
    with col56:
        st.markdown("<h5 style='text-align:center; color: white'>Fifa 2023</h5>", unsafe_allow_html=True)
        st.markdown(
            f'<div style="display: flex; justify-content: center;">'
            f'<img src="https://i.postimg.cc/bv5pP5T8/fifa2023.jpg" width="200">'
            f'</div>',
            unsafe_allow_html=True
        )
        st.markdown("<h5 style='text-align: center;'><a href='https://jugadores2023.streamlit.app/'>Link</a></h5>", unsafe_allow_html=True)
    with col57:
        st.markdown("<h5 style='text-align:center; color: white'>Futbol argentino</h5>", unsafe_allow_html=True)
        st.markdown(
            f'<div style="display: flex; justify-content: center;">'
            f'<img src="https://i.postimg.cc/wTSwXgS5/preserntation.jpg" width="200">'
            f'</div>',
            unsafe_allow_html=True
        )
        st.markdown("<h5 style='text-align: center;'><a href='https://futbolargentino.streamlit.app'>Link</a></h5>", unsafe_allow_html=True)
    

st.markdown("")
st.markdown("")

centrar_texto("About me", 1, "white")

centrar_texto("My name is Guillermo, I'm Argentine and I've been living in Brazil since November 2016. Married, my wife is Brazilian, her name is Samella, and so are my children. I have an almost three year old son named Benício Luca and an almost 9 year old daughter called Ester Valentina. I also have another 24-year-old son in Argentina from my first marriage, named Juan Ignacio and nickname Nacho.", 7, "white")
centrar_texto(" Most of my professional experience was in Argentina. Here in Brazil, most of the time I was a tourism-oriented micro entrepreneur, I organized and sold tours to different beaches on the coast of Alagoas, I made many Spanish-speaking tourists have a tourism experience without setbacks, organized and pleasant, through a page and a Facebook group that is still working: https://www.facebook.com/turismomaceioenespanol", 7, "white")
centrar_texto("During part of 2018 and all of 2019 I had my own inn two streets from the beach in the beautiful neighborhood of Pajuçara, in Maceió, called Lupita Hostel e Pousada.", 7, "white")
centrar_texto("During and after the pandemic, I manufactured and sold, as a micro-enterprise, alfajores with recipes from my city, all homemade @alfajor.milagros on instagram.", 7, "white")
centrar_texto("My professional experience in Argentina includes sales at Unifon, a company dedicated to cell phone services. I even had my own sales team and sub-agency. Organized events, stands, trained employees in sales techniques. This is when I started making my first sales reports in Excel in 1996.", 7, "white")
centrar_texto("After leaving Unifon, I became part of Parmalat Argentina in my city, Mar del Plata. Here I worked as a supervisor of a team of stockers / sales promoters. In addition to helping my team with sales and doing commercial management with the different managers of the local supermarket chains, I was also in charge of making the employee's routes. The administrative part also had a lot of spreadsheets in Excel, so thanks to this work I continued to improve my learning in statistical analysis.", 7, "white")
centrar_texto("At Nokia in 2006, I joined as head of the area, or as they later called my position, Field Supervisor. My tasks, in addition to supervising a team of 16 people in the province of Buenos Aires, and part of La Pampa, were also organizing events, coaching, team metrics, weekly meetings with my team, weekly meetings with my bosses, sales analysis, commercial management with retail managers and cell phone agents, periodic presentations to my bosses of my area's metrics, presentation of my team's metrics, in addition to debating ideas on how to always improve sales.", 7, "white")
centrar_texto(" Summary: Almost all jobs I had had metrics, data, statistical analysis, sales analysis, which I had to do and/or analyze always using Excel. Thanks to that, I became experienced, and one thing that I really enjoy doing are the formulas, in addition to the functions that the software already has that are of great help for the ETL work. As my curiosity is great, I was always worried about how I would solve the fact that Excel has its limitations, that's how I became interested in the data analyst profession when I started doing research on how to solve this fact. As I advanced in research I saw that I had many more tools, equal or more exciting than Excel, to do different tasks. SQL, Python and Power Bi. That's how I started studying Python in a self-taught way, and how I later enrolled in the Google Data Analytics PT by Coursera course to give my study a little more order. In addition, I continue to perfect myself in the different tools that the course sometimes appears only superficially.", 7, "white")
centrar_texto("My curious, detail-oriented and perfectionist nature makes me not stop studying and continue perfecting myself. There is always some new tool, for me, that facilitates the work of an analyst.", 7, "white")

st.title("")
centrar_texto("Academic training", 1, "white")
centrar_texto("Profissional Google Data Analytics by Coursera", 4, "white")

with st.container():
    col201, col202, col203, col204 = st.columns(4)
    with col202:
        centrar_texto("Share data with the art of visualization", 7, "white")
        centrar_texto("Data analysis with R programming", 7, "white")
        centrar_texto("Analyze data to answer questions", 7, "white")
        centrar_texto("Fundamentals: Data, Data, Everywhere", 7, "white")
        centrar_texto("Process the data to clean it", 7, "white")
        centrar_texto("Prepare Data for Exploration", 7, "white")
        centrar_texto("Google Data Analytics Final Project: Complete a Case Study", 7, "white")
        centrar_texto("Ask questions to make data-driven decisions", 7, "white")
    with col203:
        centrar_imagen("https://i.postimg.cc/nrSXrRzC/Titulo-coursera.jpg", 350)
        st.markdown("[Title link](https://www.coursera.org/account/accomplishments/professional-cert/LMTDNASPE8WP)")
        
st.title("")
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
st.write("---")

