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
    page_icon="📊",
    layout="wide"
)

# We reduced the empty space at the beginning of the streamlit
reduce_space ="""
            <style type="text/css">
            /* Removes space in default header of Streamlit apps */
            div[data-testid="stAppViewBlockContainer"]{
                padding-top:0px;
            }
            </style>
            """
# We load reduce_space
st.html(reduce_space)

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
def left_image(imagen, ancho):
    # Aplicar estilo CSS para centrar la imagen con Markdown
    st.markdown(
        f'<div style="display: flex; justify-content: left;">'
        f'<img src="{imagen}" width="{ancho}">'
        f'</div>',
        unsafe_allow_html=True
    )
def right_image(imagen, ancho):
    # Aplicar estilo CSS para centrar la imagen con Markdown
    st.markdown(
        f'<div style="display: flex; justify-content: right;">'
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

def circular_picture(image, img_width, align="center"):
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">', unsafe_allow_html=True)
    circulo = f"""
                <div style="text-align: {align};">
                    <img src={image} alt="" class="circle responsive-img" width="{img_width}px> <!-- notice the "circle" class -->
                </div>  
                """
    st.markdown(circulo, unsafe_allow_html=True)

def centrar_texto(texto, tamanho, color):
    st.markdown(f"<h{tamanho} style='text-align: center; color: {color}'>{texto}</h{tamanho}>",
            unsafe_allow_html=True)

def left_text(texto, tamanho, color):
    st.markdown(f"<h{tamanho} style='text-align: left; color: {color}'>{texto}</h{tamanho}>",
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
# "https://github.com/Willy71/background/blob/main/picture/Background.png?raw=true"

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
centrar_imagen("https://github.com/Willy71/background/blob/main/picture/nombre-removebg.png?raw=true" , 500)

with st.container():
    col400, col401 = st.columns([4,5])
    with col400:
        right_image('https://github.com/Willy71/background/blob/main/picture/002.png?raw=true', 300)
        #right_image('https://i.postimg.cc/Jh4cxZ5k/willy-004.png', 300)
    with col401:
        st.subheader("")
        centrar_imagen("https://github.com/Willy71/background/blob/main/picture/Analista%20de%20dados.png?raw=true", 400)
        #centrar_texto("", 5, "white")
        #centrar_texto("Data analyst,", 2, 'white')
        #centrar_texto("Business analyst", 2, 'white')
        #centrar_texto("and Python developer.", 2, 'white')

line(6, "blue")

with st.container():
    col00, col01 = st.columns(2)
    with col00:
        #st.markdown("<h1 style='text-align: center; color: white'>Objective</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: white'>Bem-vindo ao meu site, que foca em mostrar meu trabalho. O objetivo é que avaliem meu desempenho e habilidades. Python, SQL, ETL, Streamlit, Jira, Miro, Figma e Storytelling são as ferramentas mais usadas no meu trabalho.</h4>", unsafe_allow_html=True)
        #st.write(
            #"[Work done with Streamlit >](https://uberviajes.streamlit.app/)")
    with col01:
        st.markdown(
            f'<div style="display: flex; justify-content: center;">'
            f'<img src="https://i.postimg.cc/SKH4CZbD/laptop.jpg", width="300">'
            f'</div>',
            unsafe_allow_html=True
        )

line(6, "blue")



col30, col31, col32 = st.columns([0.4,6,0.4])
with col31:
    centrar_texto("Sobre mim", 1, "white")
    st.text("")
    centrar_texto(f'Sou argentino residente no Brasil desde 2016 com diversas experiências profissionais, principalmente em turismo como microempreendedor comandando o Lupita Hostel e Pousada em Maceió. Atualmente trabalho como freelancer na plataforma Upwork e também com trabalhos personalizados para clientes na cidade de Ponta Grossa, Paraná, Brasil.', 5, 'white')
    st.text("")
    centrar_texto('Minha carreira na Argentina incluiu funções de vendas, gerenciamento de equipe de vendas e supervisão. Entrei para a Nokia em 2006 como supervisor de campo, organizando eventos e participando de vendas e gestão comercial. Ao longo da minha carreira, trabalhei consistentemente com métricas, dados e análise estatística, principalmente usando o Excel.  ', 5, 'white')
    st.text("")
    centrar_texto('Meu interesse em análise de dados me levou a explorar ferramentas como SQL, Python, Streamlit e Power BI. Sou um programador Python e me matriculei no curso Google Data Analytics PT no Coursera para estruturar melhor meus estudos. Sou um analista funcional que se formou em um curso ministrado pela Silvertech Argentina. Minha curiosidade e dedicação me levam a aprender e aprimorar minhas habilidades continuamente.', 5, 'white') 

line(6, "blue")

centrar_texto("Alguns dos meus trabalhos", 1, "white")

st.text("")

with st.container():    
    col15, col16, col17, col18 = st.columns(4)
    with col15:
        centrar_imagen_link("https://github.com/Willy71/background/blob/main/picture/Coursera.png?raw=true", "https://chicagobike.streamlit.app/", "Study Case Coursera", 210) 
    with col16:
        centrar_imagen_link("https://github.com/Willy71/background/blob/main/picture/Miniatura%20-%20Analista%20funcional.png?raw=true", 'https://confort.streamlit.app/', "Nova funcionalidade", 210)
    with col17:
        centrar_imagen_link("https://github.com/Willy71/vk_tarefa1/blob/main/picture/Marketing.png?raw=true", "https://vktarefa1.streamlit.app/", "Planejamento estratégico", 220)   
    with col18:
        centrar_imagen_link("https://github.com/Willy71/background/blob/main/picture/Portfolio%20011.png?raw=true", "https://oficinamecanicapg.onrender.com/", "Gestão de oficinas mecánicas", 220)
        #centrar_imagen_link("https://github.com/Willy71/vk_tarefa1/blob/main/picture/Marketing.png?raw=true", "https://vktarefa1.streamlit.app/", "Planejamento estratégico", 220)
        #centrar_imagen_link("https://i.postimg.cc/XvjGtYrT/preserntation.jpg", 'https://futbolargentino.streamlit.app', "Futbol liga Argentina", 215)
    #with col19:
        #centrar_imagen("https://i.postimg.cc/MHK9TS34/Hotel001.jpg", 205)
        #centrar_imagen_link("https://i.postimg.cc/MHK9TS34/Hotel001.jpg", "Hotel", 205)
        #"https://hotelservice.streamlit.app/"
        #centrar_imagen_link("https://i.postimg.cc/h45LxTXh/streamlit-page.jpg", 'https://github.com/Willy71/background/', "Sitio web com Python",200)    
    
   
with st.container():    
    col10, col11, col12, col13 = st.columns(4)
    with col10:
        centrar_imagen_link("https://i.postimg.cc/MHK9TS34/Hotel001.jpg", 'https://hotelservice.streamlit.app/', "Hotel Service",200)         
    with col11:
        centrar_imagen_link("https://github.com/Willy71/background/blob/main/picture/Portfolio%20012.png?raw=true", 'https://crm-oficinas.onrender.com/', "CRM Leads", 200)
    with col12:
        centrar_imagen_link("https://i.postimg.cc/nrR09P6L/lavajato.jpg", 'https://github.com/Willy71/washcar', "Lava-jato", 175)
    with col13:
        centrar_imagen_link('https://i.postimg.cc/ZRLf4RHp/Estacionamiento.jpg', 'https://github.com/Willy71/parking', "Estacionamento", 160)
    #with col11:
        #centrar_imagen_link("https://i.postimg.cc/wx0Wr17d/super003.jpg", 'https://github.com/Willy71/supermercados', "Supermercado", 200)
        #centrar_imagen_link("https://i.postimg.cc/X7Bwgq5L/uber-ny.jpg", "https://uberviajes.streamlit.app/", "Uber - New York", 220)
        #centrar_imagen_link("https://i.postimg.cc/0yJcrZZ8/tareas001.jpg", 'https://github.com/Willy71/tareas',"Daily task manager", 210)     
              
line(6, "blue")

centrar_texto("Formação acadêmica", 1, "white")
centrar_texto("Profissional Google Data Analytics by Coursera", 4, "white")
st.title("#")
with st.container():
    col20, col21, col22, col23, col500 = st.columns([1,3.3,0.3,3.3,1])
    with col21:
        centrar_texto("1- Fundamentos: Dados, em todo lugar", 7, "white")
        centrar_texto("2- Faça perguntas para tomar decisões baseadas em dados", 7, "white")
        centrar_texto("3- Preparar dados para exploração", 7, "white")
        centrar_texto("4- Processe os dados para limpá-los", 7, "white")
        centrar_texto("5- Analisar dados para responder perguntas", 7, "white")  
        centrar_texto("6- Compartilhe dados com a arte da visualização", 7, "white")
        centrar_texto("7- Análise de dados com programação R", 7, "white")
        centrar_texto("8- Projeto final do Google Data Analytics: Concluir um estudo de caso", 7, "white")

    with col23:
        centrar_imagen_link("https://i.postimg.cc/zG347njM/Titulo-coursera.jpg", 'https://www.coursera.org/account/accomplishments/professional-cert/LMTDNASPE8WP', 'Title link',  350)

line(6, "blue")

#=====================================================================================================================================================================
# Recomendations

with st.container():
    col500, col501, col502 = st.columns([2, 5, 2])
    with col501:
        centrar_texto("Recomendações no Linkedin", 1, "white")
        centrar_texto("",5,"white")
        with st.container():
            col301, col302, col303, col304 = st.columns([0.5,1,2,0.5])
            with col302:
                centrar_imagen("https://i.postimg.cc/nzC8LgR3/rodrigo-campos-remove.png", 150)
            with col303:
                centrar_texto_link('Rodrigo Campos', "https://www.linkedin.com/in/rodrigocampos/", 4, 'lightblue')
                centrar_texto_link('Key account manager - Mobile Executive Leader | Driving Performance & Growth | INSEAD Exec. MBA & Harvard alumnus, Doctoral Candidate', "https://www.linkedin.com/in/rodrigocampos/", 4, 'lightblue')
        st.text("")
        left_text("I am glad to recommend Guillermo, with whom I had the opportunity of working at Nokia. Guillermo stands out for his exceptional blend of experience in business, leadership, marketing operations, and advanced analytics.", 4, 'white')
        left_text(" ", 4, "white")
        left_text("He possesses the unique ability to extract actionable insights from complex data sets without losing sight of operational realities. Guillermo takes ownership of his responsibilities passionately and diligently, consistently delivering work of outstanding quality. Guillermo's dedication and sense of responsibility make him an invaluable asset to any team. I am confident that he will continue to excel and bring his exceptional skills", 4, "white")  
        
        line(3, "blue")

        
        with st.container():
            col305, col306, col307, col308 = st.columns([0.5,1,1.5,1])
            with col306:
                centrar_imagen("https://i.postimg.cc/J41hr43x/maxi-remove.png", 150)
            with col307:
                centrar_texto_link('Maximiliano Roca Saran', "https://www.linkedin.com/in/maximiliano-roca-0b628421/", 4, 'lightblue')
                centrar_texto_link('Key account manager - Mobile phones', "https://www.linkedin.com/in/maximiliano-roca-0b628421/", 4, 'lightblue')
        st.text("")
        left_text('Guilherme é um excelente gestor, sempre predisposto, muito focado no que faz e orientado a resultados. Ele é um ótimo construtor de equipamentos de trabalho. Ele está sempre disposto a aprender coisas novas e mudar.', 4, 'white')
        
        line(3, "blue")
        
        with st.container():
            col309, col310, col311, col312 = st.columns([0.5,1,1.5,1])
            with col310:
                centrar_imagen("https://i.postimg.cc/qMt5C2Gv/cristina-remove.png", 150)
            with col311:
                centrar_texto_link('Cristina Jacquemin', "https://www.linkedin.com/in/jacquemin-cristina-51958027/", 4, 'lightblue')
                centrar_texto_link('Accounts director - Grupo Solvens', "https://www.linkedin.com/in/jacquemin-cristina-51958027/", 4, 'lightblue')
        st.text("")
        left_text("O Guillermo é sem dúvida um grande profissional na sua área, um grande líder e gerador de equipes de trabalho eficientes!", 4, "white")
        
        line(3, "blue")
        
        with st.container():
            col313, col314, col315, col316 = st.columns([0.5,1,1.5,1])
            with col314:
                centrar_imagen("https://i.postimg.cc/Y9WxCxH5/ariel-remove.png", 150)
            with col315:
                centrar_texto_link("Ariel Smirnoff", "https://www.linkedin.com/in/ariel-smirnoff-b85094b0/", 4, 'lightblue')
                centrar_texto_link("Business coach", "https://www.linkedin.com/in/ariel-smirnoff-b85094b0/", 4, 'lightblue')
        st.text("")
        left_text("O Guillermo sempre foi super atencioso com sua equipe, mas também exigente, acompanhando cada um em suas necessidades e desenvolvendo pessoal para o qual trabalhava de forma estruturada através de planos  de ação, o que lhe permitia verificar se o colaborador não sabia (ele os ensinava) ;se eu não pudesse (eu ajudei ele); mas se ele não quisesse não havia perda de tempo.  ", 4, "white")
        left_text("Super orientado a resultados. Confiável no atendimento ao cliente (varejistas) e desenvolvimento de território, ticket médio, arpu, ROI, participação de  mercado, visibilidade de marca e treinamento de varejistas. Sempre se mostrou com profissionalismo,  entusiasmo e rapidez, a equipe que liderou obteve resultados e expandiu a área. Também surgiram  colaboradores que conseguiram crescer e se desenvolver sob sua direção. ", 4, "white") 

        
        line(3, "blue")
        
        with st.container():
            col317, col318, col319, col320 = st.columns([0.5,1,1.5,1])
            with col318:
                centrar_imagen("https://i.postimg.cc/MHrZ31cG/agustin-remove.png", 150)
            with col319:
                centrar_texto_link("Agustin Valdes Marteles", "https://www.linkedin.com/in/agustin-valdes-marteles-55273022/", 3, 'lightblue')
                centrar_texto_link("Make it happen", "https://www.linkedin.com/in/agustin-valdes-marteles-55273022/", 3, 'lightblue')
        st.text("")
        left_text("Excelente pessoa e excelente profissional. Muito humano e ideal para a posição em que partilhamos companhia. Foi um prazer trabalhar com ele.", 4, "white") 
        
          
line(6, "blue")

st.markdown("<h1 style='text-align: center; color: white'>Contato</h1>", unsafe_allow_html=True)
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

line(6, "blue")

#=====================================================================================================================================================================
# Send an email

centrar_texto('Envie um email 💌', 1, 'white')

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

line(6, "blue")

#=====================================================================================================================================================================

with st.container():
    col51, col52 = st.columns(2)
    with col51:
        st.markdown("<h2 style='text-align: center; color: white'>Site feito com Streamlit</h2>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: blue;'>Programado com Python</h2>", unsafe_allow_html=True)
    with col52:
        co53, col54, col55, col56, col57 = st.columns(5)
        with col54:            
            st.text(" ")
            st.text(" ")
            centrar_imagen("https://i.postimg.cc/cJhYJnqx/streamlit-logo.jpg", 150)
        with col56:
            centrar_imagen("https://i.postimg.cc/9Q3yg2th/python.png", 150)
            
line(6, "blue")







