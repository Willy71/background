import streamlit as st
import requests
from PIL import Image
import base64
from datetime import datetime
from dateutil.relativedelta import relativedelta
from streamlit_gtag import st_gtag
import smtplib
from email.mime.text import MIMEText

# Colocar nome na pagina, icone e ampliar a tela
st.set_page_config(
    page_title="Portfolio - Guillermo Cerato",
    page_icon="💻",
    layout="wide"
)

######################################################################################################################
# Google Analitycs

st_gtag(
    key="gtag_send_event_page_load",
    id="G-WKF4W6RNR3",
    event_name="app_main_page_load",
    params={
        "event_category": "page_load",
        "event_label": "main_page",
        "value": 1,
    },
)

#G-RZECDKJY1Z
######################################################################################################################

def calcular_edad(fecha_nac):
    fecha_nac = datetime.strptime(fecha_nac, '%d/%m/%Y')
    now = datetime.now()
    # Al usar relativedelta, se tienen en cuenta los años bisiestos para calcular edad
    # La otra forma es hacerlo con deltamime y dividir por 365, pero no es un calculo exacto
    diferencia = relativedelta(now, fecha_nac)
    edad_anios = diferencia.years

    return edad_anios

edad_willy = calcular_edad('14/02/1971')
edad_benicio = calcular_edad('27/11/2020')
edad_nacho = calcular_edad('11/03/1999')
edad_ester = calcular_edad('21/12/2014')

def photo_link(alt_text, img_url, link_url, img_width):
    markdown_code = f'<a href="{link_url}" target="_blank"><img src="{img_url}" alt="{alt_text}" width="{img_width}px"></a>'
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

def centrar_texto_link(link_texto, link_url, tamanho, color):
    texto_html = f"<h{tamanho} style='text-align: center; color: {color}'><a href='{link_url}' target='_blank'>{link_texto}</a></h{tamanho}>"
    st.markdown(texto_html, unsafe_allow_html=True)

def line(size, color):
    st.markdown(f"<hr style= height:{size}px;border:none;color:{color};background-color:{color}; />",
                unsafe_allow_html=True)
    return

######################################################################################################################
# Background

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://raw.githubusercontent.com/Willy71/background/main/picture/pxfuel%20(1).jpg");
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

######################################################################################################################
st.write("#")
centrar_imagen("https://github.com/Willy71/background/blob/main/picture/nombre-removebg.png?raw=true" , 500)
centrar_imagen('https://i.postimg.cc/Jh4cxZ5k/willy-004.png', 300)
centrar_texto("Data analyst, Business analyst and Python developer.", 2, 'white')

line(6, "blue")
#st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

with st.container():
    col00, col01 = st.columns(2)
    with col00:
        #st.markdown("<h1 style='text-align: center; color: white'>Objective</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: white'>Welcome to my website, which focuses on showcasing my work. The objective is for them to evaluate my performance and skills. Python, SQL, Excel, Power BI, Streamlit, Jira, Miro, Figma and Storytelling are the most used tools in my work.</h4>", unsafe_allow_html=True)
        #st.write(
            #"[Work done with Streamlit >](https://uberviajes.streamlit.app/)")
    with col01:
        st.markdown(
            f'<div style="display: flex; justify-content: center;">'
            f'<img src="https://i.postimg.cc/SKH4CZbD/laptop.jpg", width="300">'
            f'</div>',
            unsafe_allow_html=True
        )

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

centrar_texto("About me", 1, "white")

col30, col31, col32 = st.columns([1,6,1])
with col31:
    centrar_texto(f'I am an Argentine resident in Brazil since 2016 with diverse professional experiences, mainly in tourism as a micro-entrepreneur running Lupita Hostel e Pousada in Maceió. I am currently working as a freelancer on the Upwork platform as well as custom work for clients in my city.', 6, 'white')
    st.text("")
    centrar_texto('My career in Argentina included sales roles at Unifon, managing their sales team, and at Parmalat as a supervisor. I joined Nokia in 2006 as a field supervisor, organizing events and participating in sales and commercial management.Throughout my career, I have consistently worked with metrics, data, and statistical analysis, primarily using Excel.  ', 6, 'white')
    st.text("")
    centrar_texto('My interest in data analysis led me to explore tools like SQL, Python, Streamlit and Power BI. I am a Python programmer and enrolled in the Google Data Analytics PT course on Coursera to further structure my studies. I am a Business analyst who graduated from a course taught by Silvertech Argentina. My curiosity and dedication drive me to continually learn and hone my skills in data analytics.', 6, 'white') 

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white'>Works</h1>", unsafe_allow_html=True)

st.text("")

with st.container():    
    col15, col16, col17, col18, col19 = st.columns(5)
    with col15:
        centrar_imagen_link("https://github.com/Willy71/background/blob/main/picture/Cover_002.png?raw=true", "https://chicagobike.streamlit.app/", "Study Case Coursera", 210) 
    with col16:
        centrar_imagen_link("https://i.postimg.cc/X7Bwgq5L/uber-ny.jpg", "https://uberviajes.streamlit.app/", "Uber - New York", 220)
    with col17:
        centrar_imagen_link("https://i.postimg.cc/MHK9TS34/Hotel001.jpg", 'https://hotelservice.streamlit.app/', "Hotel Service",200)  
        #centrar_imagen("https://i.postimg.cc/MHK9TS34/Hotel001.jpg", 205)
        #centrar_imagen_link("https://i.postimg.cc/MHK9TS34/Hotel001.jpg", "hotel", 205)
        #"https://hotelservice.streamlit.app/"
    with col18:
        centrar_imagen_link("https://i.postimg.cc/XvjGtYrT/preserntation.jpg", 'https://futbolargentino.streamlit.app', "Soccer Argentina", 215)
    with col19:
        centrar_imagen_link("https://i.postimg.cc/h45LxTXh/streamlit-page.jpg", 'https://github.com/Willy71/background/', "Web page with Python",200)    
    
   



with st.container():    
    col10, col11, col12, col13, col14 = st.columns(5)
    with col10:
        centrar_imagen_link("https://github.com/Willy71/background/blob/main/picture/Miniatura%20-%20Analista%20funcional.png?raw=true", 'https://confort.streamlit.app/', "business analyst job", 210)       
    with col11:
        centrar_imagen_link("https://i.postimg.cc/wx0Wr17d/super003.jpg", 'https://github.com/Willy71/supermercados', "Supermarket", 200) 
    with col12:
        centrar_imagen_link("https://i.postimg.cc/0yJcrZZ8/tareas001.jpg", 'https://github.com/Willy71/tareas',"Daily task manager", 210)
    with col13:
        centrar_imagen_link("https://i.postimg.cc/nrR09P6L/lavajato.jpg", 'https://github.com/Willy71/washcar', "Washcar", 175)
    with col14:
        centrar_imagen_link('https://i.postimg.cc/ZRLf4RHp/Estacionamiento.jpg', 'https://github.com/Willy71/parking', "Parking", 160)
              
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

centrar_texto("Academic training", 1, "white")
centrar_texto("Profissional Google Data Analytics by Coursera", 4, "white")
st.title("#")
with st.container():
    col20, col21, col22, col23, col500 = st.columns([1,3.3,0.3,3.3,1])
    with col21:
        centrar_texto("1- Fundamentals: Data, Data, Everywhere", 7, "white")
        centrar_texto("2- Ask questions to make data-driven decisions", 7, "white")
        centrar_texto("3- Prepare Data for Exploration", 7, "white")
        centrar_texto("4- Process the data to clean it", 7, "white")
        centrar_texto("5- Analyze data to answer questions", 7, "white")  
        centrar_texto("6- Share data with the art of visualization", 7, "white")
        centrar_texto("7- Data analysis with R programming", 7, "white")
        centrar_texto("8- Google Data Analytics Final Project: Complete a Case Study", 7, "white")

    with col23:
        centrar_imagen_link("https://i.postimg.cc/zG347njM/Titulo-coursera.jpg", 'https://www.coursera.org/account/accomplishments/professional-cert/LMTDNASPE8WP', 'Title link',  350)

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
        
centrar_texto("Recommendations in Linkedin", 1, "white")
st.title("")
with st.container():
    col301, col302, col303, col304 = st.columns([0.5,1,2,0.5])
    with col302:
        centrar_imagen("https://i.postimg.cc/nzC8LgR3/rodrigo-campos-remove.png", 150)
    with col303:
        centrar_texto_link('Rodrigo Campos', "https://www.linkedin.com/in/rodrigocampos/", 4, 'lightblue')
        centrar_texto_link('Key account manager - Mobile Executive Leader | Driving Performance & Growth | INSEAD Exec. MBA & Harvard alumnus, Doctoral Candidate', "https://www.linkedin.com/in/rodrigocampos/", 4, 'lightblue')
st.text("")
centrar_texto("I am glad to recommend Guillermo, with whom I had the opportunity of working at Nokia.", 6, 'white')
centrar_texto(" Guillermo stands out for his exceptional blend of experience in business, leadership, marketing operations, and advanced analytics.", 6, "white")
centrar_texto("He possesses the unique ability to extract actionable insights from complex data sets without losing sight of operational realities.", 6, "white")  
centrar_texto("Guillermo takes ownership of his responsibilities passionately and diligently, consistently delivering work of outstanding quality.", 6, "white")  
centrar_texto("Guillermo's dedication and sense of responsibility make him an invaluable asset to any team.", 6, "white")  
centrar_texto("I am confident that he will continue to excel and bring his exceptional skills.", 6, "white")
st.title("")

with st.container():
    col305, col306, col307, col308 = st.columns([0.5,1,1.5,1])
    with col306:
        centrar_imagen("https://i.postimg.cc/J41hr43x/maxi-remove.png", 150)
    with col307:
        centrar_texto_link('Maximiliano Roca Saran', "https://www.linkedin.com/in/maximiliano-roca-0b628421/", 4, 'lightblue')
        centrar_texto_link('Key account manager - Mobile phones', "https://www.linkedin.com/in/maximiliano-roca-0b628421/", 4, 'lightblue')
st.text("")
centrar_texto('Guillermo is an excellent manager, always predisposed, very focused on what he does and results-oriented.', 6, 'white')
centrar_texto("He is a very good team builder. He is always willing to learn new things and change.", 6, "white")
st.title("")

with st.container():
    col309, col310, col311, col312 = st.columns([0.5,1,1.5,1])
    with col310:
        centrar_imagen("https://i.postimg.cc/qMt5C2Gv/cristina-remove.png", 150)
    with col311:
        centrar_texto_link('Cristina Jacquemin', "https://www.linkedin.com/in/jacquemin-cristina-51958027/", 4, 'lightblue')
        centrar_texto_link('Accounts director - Grupo Solvens', "https://www.linkedin.com/in/jacquemin-cristina-51958027/", 4, 'lightblue')
st.text("")
centrar_texto("Guillermo is without a doubt a great professional in his area, a great leader and generator of efficient work teams!", 6, "white")
st.title("")

with st.container():
    col313, col314, col315, col316 = st.columns([0.5,1,1.5,1])
    with col314:
        centrar_imagen("https://i.postimg.cc/Y9WxCxH5/ariel-remove.png", 150)
    with col315:
        centrar_texto_link("Ariel Smirnoff", "https://www.linkedin.com/in/ariel-smirnoff-b85094b0/", 4, 'lightblue')
        centrar_texto_link("Business coach", "https://www.linkedin.com/in/ariel-smirnoff-b85094b0/", 4, 'lightblue')
st.text("")
centrar_texto("Guillermo was always super considerate of his team, but also demanding, accompanying each one in their needs and", 6, "white")
centrar_texto("developing personnel for which he worked in a structured way through action plans, which allowed him to check if the collaborator", 6, "white") 
centrar_texto("did not know (he taught them) ; if he couldn't (help him); but if he didn't want to there was no waste of time.Super results oriented.", 6, "white") 
centrar_texto("Reliable in customer service (retailers) and territory development, average ticket, arpu, ROI, market share, brand visibility,", 6, "white") 
centrar_texto("and retailer training. He always showed himself with professionalism, enthusiasm and speed, the team he led achieved results and", 6, "white") 
centrar_texto("expanded the area. Collaborators also emerged who were able to grow and develop under his direction.", 6, "white")
st.title("")

with st.container():
    col317, col318, col319, col320 = st.columns([0.5,1,1.5,1])
    with col318:
        centrar_imagen("https://i.postimg.cc/MHrZ31cG/agustin-remove.png", 150)
    with col319:
        centrar_texto_link("Agustin Valdes Marteles", "https://www.linkedin.com/in/agustin-valdes-marteles-55273022/", 4, 'lightblue')
        centrar_texto_link("Make it happen", "https://www.linkedin.com/in/agustin-valdes-marteles-55273022/", 4, 'lightblue')
st.text("")
centrar_texto("Excellent person and excellent professional. Very human and ideal for", 6, "white") 
centrar_texto("the position in which we share company. It has been a pleasure to work with him.", 6, "white")
st.title("")

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white'>Contact</h1>", unsafe_allow_html=True)
st.text("")

with st.container():    
    col41, col42, col43 = st.columns(3)
    with col41:
        centrar_imagen("https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/189_Kaggle_logo_logos-512.png", 80)
        centrar_texto_link("Kaggle", "https://www.kaggle.com/willycerato", 6, 'white')
    with col42:
        centrar_imagen("https://cdn.pixabay.com/photo/2022/01/30/13/33/github-6980894_1280.png", 80)
        centrar_texto_link("Github", "https://github.com/Willy71", 6, 'white')
    with col43:
        centrar_imagen("https://img.freepik.com/vetores-premium/logotipo-quadrado-do-linkedin-isolado-no-fundo-branco_469489-892.jpg", 80)
        centrar_texto_link("Linkedin", "https://www.linkedin.com/in/willycerato",  6, 'white')
    st.caption("")
    col44, col45, col46 = st.columns(3)
    with col44:
        centrar_imagen("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/2023_Facebook_icon.svg/50px-2023_Facebook_icon.svg.png", 80)
        centrar_texto_link("Facebook", "https://www.facebook.com/guillermo.cerato", 6, 'white')
    with col45:
        centrar_imagen("https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Instagram_logo_2022.svg/150px-Instagram_logo_2022.svg.png", 80)
        centrar_texto_link("Instagram", "https://www.instagram.com/willycerato", 6 ,'white')
    with col46:
        centrar_imagen("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/120px-WhatsApp.svg.png", 80)
        centrar_texto_link("Whatsapp", "https://wa.me/5542991657847", 6, 'white')

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

centrar_texto('Send an email 💌', 1, 'white')

with st.container():
    co01, co02, co03 = st.columns([2, 4, 2])
    with co02:
        # Taking inputs
        email_sender = 'gcerato@gmail.com'
        email_receiver = 'gcerato@gmail.com'
        email = st.text_input("Email")
        subject = st.text_input('Subject')
        body = st.text_area('Body')
        total = ("Portfolio \n" + body + "\n" + email)

        if st.button("Send Email"):
            try:
                msg = MIMEText(total)
                msg['From'] = email_sender
                msg['To'] = email_receiver
                msg['Subject'] = subject

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(st.secrets["email"]["gmail"], st.secrets["email"]["password"])
                server.sendmail(email_sender, email_receiver, msg.as_string())
                server.quit()
        
                st.success('Email sent successfully! 🚀')
            except Exception as e:
                st.error(f"Failed to send email: {e}")

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

with st.container():
    col51, col52 = st.columns(2)
    with col51:
        st.markdown("<h2 style='text-align: center; color: white'>Website made with Streamlit</h2>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: blue;'>Programmed with Python</h2>", unsafe_allow_html=True)
    with col52:
        co53, col54, col55, col56, col57 = st.columns(5)
        with col54:            
            st.text(" ")
            st.text(" ")
            photo_link('', "https://i.postimg.cc/cJhYJnqx/streamlit-logo.jpg", 'https://streamlit.io/', 150)
        with col56:
            photo_link('', "https://i.postimg.cc/9Q3yg2th/python.png", 'https://www.python.org', 150)
            
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)



