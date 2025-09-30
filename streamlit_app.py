import streamlit as st
import requests
from PIL import Image
import smtplib
from email.mime.text import MIMEText

# Set the page configuration
# This should be the first Streamlit command in your script
st.set_page_config(
    page_title="Guillermo Cerato's Portfolio",
    page_icon="📊",
    layout="wide"
)

# --- META TAGS FOR SOCIAL MEDIA SHARING (NEW CODE) ---
# This block adds the necessary tags for link previews on social media.
st.markdown("""
    <meta property="og:title" content="Guillermo Cerato's Portfolio">
    <meta property="og:description" content="Data Analyst and Python Developer. Explore my projects and skills.">
    <meta property="og:image" content="https://raw.githubusercontent.com/Willy71/background/main/picture/002.png">
    <meta property="og:url" content="https://guillermocerato.streamlit.app">
    <meta name="twitter:card" content="summary_large_image">
""", unsafe_allow_html=True)


# --- HELPER FUNCTIONS ---

def centrar_texto(texto, tamanho, color):
    """Centers text using HTML."""
    st.markdown(f"<h{tamanho} style='text-align: center; color: {color}'>{texto}</h{tamanho}>",
                unsafe_allow_html=True)

def centrar_imagen(src, width):
    """Centers an image using HTML."""
    st.markdown(
        f'<div style="display: flex; justify-content: center;">'
        f'<img src="{src}" width="{width}">'
        f'</div>',
        unsafe_allow_html=True
    )

def centrar_imagen_link(img_src, link_url, alt_text, width):
    """Centers an image that is also a hyperlink."""
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <a href="{link_url}" target="_blank">
                <img src="{img_src}" width="{width}" alt="{alt_text}" style="border-radius: 10px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);">
            </a>
        </div>
        <h5 style='text-align: center; margin-top: 10px;'><a href='{link_url}' target="_blank" style="color: white; text-decoration: none;">{alt_text}</a></h5>
        """,
        unsafe_allow_html=True
    )

def line(size, color):
    """Creates a horizontal line."""
    st.markdown(f"<hr style='height:{size}px; border:none; color:{color}; background-color:{color};' />",
                unsafe_allow_html=True)

# --- PAGE STYLING ---

# Reduce the empty space at the top of the page
st.markdown("""
    <style type="text/css">
        div[data-testid="stAppViewBlockContainer"] {
            padding-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Set the background image
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://raw.githubusercontent.com/Willy71/background/main/picture/pxfuel%20(1).jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
[data-testid="stHeader"], [data-testid="stToolbar"] {
    background: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


# --- HEADER SECTION ---
centrar_imagen("https://github.com/Willy71/background/blob/main/picture/nombre-removebg.png?raw=true", 500)

with st.container():
    col1, col2 = st.columns([4, 5])
    with col1:
        centrar_imagen('https://github.com/Willy71/background/blob/main/picture/002.png?raw=true', width=300)
    with col2:
        st.write("") # Vertical spacer
        st.write("") # Vertical spacer
        centrar_imagen("https://github.com/Willy71/background/blob/main/picture/Gemini_Generated_Image_001.png?raw=true", 400)

line(6, "blue")

# --- INTRODUCTION ---
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h4 style='text-align: center; color: white; padding: 1rem;'>Welcome to my portfolio. Here, I showcase my projects and skills as a Data Analyst and Python Developer. My goal is to transform complex data into strategic decisions.</h4>", unsafe_allow_html=True)
    with col2:
        centrar_imagen("https://i.postimg.cc/SKH4CZbD/laptop.jpg", 300)

line(6, "blue")

# --- ABOUT ME ---
with st.container():
    centrar_texto("About Me", 2, "white")
    st.write("")
    about_me_text = """
    <p style='text-align: center; color: white; font-size: 1.1rem; max-width: 800px; margin: auto;'>
    I am an Argentinian professional based in Brazil since 2016, with a diverse background in tourism, entrepreneurship, and team management. My career in Argentina, including key roles at Nokia, provided a strong foundation in data-driven decision-making, where I consistently used metrics and statistical analysis to drive results.
    <br><br>
    My passion for data led me to pursue expertise in tools like SQL, Python, Streamlit, and Power BI. I am a Google-certified Data Analyst and a Functional Analyst, constantly seeking to learn and refine my skills. I thrive on curiosity and dedication, turning complex datasets into actionable insights.
    </p>
    """
    st.markdown(about_me_text, unsafe_allow_html=True)

line(6, "blue")

# --- SKILLS ---
with st.container():
    centrar_texto("Technical Skills", 2, "white")
    st.write("")
    col1, col2, col3 = st.columns(3)
    with col1:
        centrar_texto("Programming & Data", 4, "lightblue")
        st.markdown("<p style='text-align: center; color: white;'>Python (Pandas, Streamlit)<br>SQL<br>ETL Processes</p>", unsafe_allow_html=True)
    with col2:
        centrar_texto("Business & Visualization", 4, "lightblue")
        st.markdown("<p style='text-align: center; color: white;'>Data Visualization (Storytelling)<br>Excel & Google Sheets<br>Google Slides</p>", unsafe_allow_html=True)
    with col3:
        centrar_texto("Tools & Methodologies", 4, "lightblue")
        st.markdown("<p style='text-align: center; color: white;'>Jira & Miro<br>Figma<br>Agile Methodologies</p>", unsafe_allow_html=True)


line(6, "blue")

# --- PORTFOLIO / PROJECTS ---
centrar_texto("My Projects", 2, "white")
st.write("")

# --- Project Row 1 ---
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        centrar_imagen_link("https://github.com/Willy71/background/blob/main/picture/Coursera.png?raw=true", "https://cyclistic-chicago.onrender.com/", "Coursera Case Study", 210)
        st.markdown("<p style='text-align: center; color: white; font-size: 0.9rem;'>Analysis of Chicago bike trip data. Used Python and Streamlit to build an interactive dashboard.</p>", unsafe_allow_html=True)
    with col2:
        centrar_imagen_link("https://github.com/Willy71/background/blob/main/picture/Miniatura%20-%20Analista%20funcional.png?raw=true", 'https://confort-j4ix.onrender.com/', "New Functionality Proposal", 210)
        st.markdown("<p style='text-align: center; color: white; font-size: 0.9rem;'>Functional analysis to design and propose a new feature for an existing application.</p>", unsafe_allow_html=True)
    with col3:
        centrar_imagen_link("https://github.com/Willy71/vk_tarefa1/blob/main/picture/Marketing.png?raw=true", "https://vk-tarefa1.onrender.com/", "Strategic Marketing Plan", 220)
        st.markdown("<p style='text-align: center; color: white; font-size: 0.9rem;'>Developed a data-driven strategic plan for a marketing campaign, identifying key segments.</p>", unsafe_allow_html=True)
    with col4:
        centrar_imagen_link("https://github.com/Willy71/background/blob/main/picture/Portfolio%20011.png?raw=true", "https://oficinamecanicapg.onrender.com/", "Mechanic Shop Management", 220)
        st.markdown("<p style='text-align: center; color: white; font-size: 0.9rem;'>A full-stack web application built with Python to manage clients, services, and billing.</p>", unsafe_allow_html=True)
st.write("")

# --- Project Row 2 ---
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        centrar_imagen_link("https://i.postimg.cc/MHK9TS34/Hotel001.jpg", 'https://hotelservice-ynsh.onrender.com', "Hotel Service App", 200)
        st.markdown("<p style='text-align: center; color: white; font-size: 0.9rem;'>Concept app for hotel service management, including bookings and room service.</p>", unsafe_allow_html=True)
    with col2:
        centrar_imagen_link("https://github.com/Willy71/background/blob/main/picture/Portfolio%20012.png?raw=true", 'https://crm-oficinas.onrender.com/', "CRM for Leads", 200)
        st.markdown("<p style='text-align: center; color: white; font-size: 0.9rem;'>A simple CRM application to track and manage sales leads for mechanic shops.</p>", unsafe_allow_html=True)
    with col3:
        centrar_imagen_link("https://i.postimg.cc/nrR09P6L/lavajato.jpg", 'https://github.com/Willy71/washcar', "Car Wash System", 175)
        st.markdown("<p style='text-align: center; color: white; font-size: 0.9rem;'>A command-line based system to manage car wash services and appointments.</p>", unsafe_allow_html=True)
    with col4:
        centrar_imagen_link('https://i.postimg.cc/ZRLf4RHp/Estacionamiento.jpg', 'https://github.com/Willy71/parking', "Parking Management", 160)
        st.markdown("<p style='text-align: center; color: white; font-size: 0.9rem;'>A Python script to simulate and manage a parking lot's occupancy and fees.</p>", unsafe_allow_html=True)


line(6, "blue")

# --- EDUCATION ---
centrar_texto("Education & Certifications", 2, "white")
st.write("")
with st.container():
    col1, col2 = st.columns([7, 3])
    with col1:
        st.markdown("<h4 style='text-align: left; color: lightblue;'>Google Data Analytics Professional Certificate</h4>", unsafe_allow_html=True)
        st.markdown("""
        <ul style='color: white;'>
            <li>Foundations: Data, Data, Everywhere</li>
            <li>Ask Questions to Make Data-Driven Decisions</li>
            <li>Prepare Data for Exploration</li>
            <li>Process Data from Dirty to Clean</li>
            <li>Analyze Data to Answer Questions</li>
            <li>Share Data Through the Art of Visualization</li>
            <li>Data Analysis with R Programming</li>
            <li>Google Data Analytics Capstone: Complete a Case Study</li>
        </ul>
        """, unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: left; color: lightblue; margin-top: 1rem;'>Functional Analyst - SilverTech Program</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: left; color: lightblue; margin-top: 1rem;'>Master's in Commercial Management (Marketing) - UADE</h4>", unsafe_allow_html=True)

    with col2:
        centrar_imagen_link("https://i.postimg.cc/zG347njM/Titulo-coursera.jpg", 'https://www.coursera.org/account/accomplishments/professional-cert/LMTDNASPE8WP', 'Certificate Link', 350)


line(6, "blue")

# --- RECOMMENDATIONS ---
with st.container():
    centrar_texto("LinkedIn Recommendations", 2, "white")
    st.write("")
    # Recommendation 1
    st.markdown("""
    <p style='text-align: center; color: white; font-style: italic; max-width: 700px; margin: auto;'>
    "I am glad to recommend Guillermo... He possesses the unique ability to extract actionable insights from complex data sets without losing sight of operational realities. Guillermo's dedication and sense of responsibility make him an invaluable asset to any team."
    </p>
    <p style='text-align: center; color: lightblue; margin-top: 0.5rem;'>
    <a href="https://www.linkedin.com/in/rodrigocampos/" target="_blank" style="color: lightblue;">Rodrigo Campos</a><br>
    Key Account Manager - Mobile Executive Leader
    </p>
    """, unsafe_allow_html=True)
    st.write("")
    st.write("")
    # Recommendation 2
    st.markdown("""
    <p style='text-align: center; color: white; font-style: italic; max-width: 700px; margin: auto;'>
    "Guillermo is an excellent manager, always predisposed, very focused on what he does, and results-oriented. He is a great team builder and is always willing to learn new things and embrace change."
    </p>
    <p style='text-align: center; color: lightblue; margin-top: 0.5rem;'>
    <a href="https://www.linkedin.com/in/maximiliano-roca-0b628421/" target="_blank" style="color: lightblue;">Maximiliano Roca Saran</a><br>
    Key Account Manager - Mobile phones
    </p>
    """, unsafe_allow_html=True)


line(6, "blue")

# --- CONTACT ---
centrar_texto("Contact Me", 2, "white")
st.write("")

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        centrar_imagen("https://cdn.pixabay.com/photo/2022/01/30/13/33/github-6980894_1280.png", 80)
        st.markdown("<p style='text-align: center;'><a href='https://github.com/Willy71' target='_blank' style='color: white; font-size: 1.1rem;'>GitHub</a></p>", unsafe_allow_html=True)
    with col2:
        centrar_imagen("https://img.freepik.com/vetores-premium/logotipo-quadrado-do-linkedin-isolado-no-fundo-branco_469489-892.jpg", 80)
        st.markdown("<p style='text-align: center;'><a href='https://www.linkedin.com/in/willycerato' target='_blank' style='color: white; font-size: 1.1rem;'>LinkedIn</a></p>", unsafe_allow_html=True)
    with col3:
        centrar_imagen("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/120px-WhatsApp.svg.png", 80)
        st.markdown("<p style='text-align: center;'><a href='https://wa.me/5542991657847' target='_blank' style='color: white; font-size: 1.1rem;'>WhatsApp</a></p>", unsafe_allow_html=True)


st.write("")
line(6, "blue")

# --- EMAIL FORM ---
centrar_texto('Send me an email 💌', 2, 'white')

with st.container():
    _, col_form, _ = st.columns([1, 2, 1])
    with col_form:
        email_sender = 'gcerato@gmail.com'
        email_receiver = 'gcerato@gmail.com'
        
        with st.form(key='contact_form'):
            user_email = st.text_input("Your Email")
            subject = st.text_input('Subject')
            body = st.text_area('Body')
            submit_button = st.form_submit_button("Send Email")

            if submit_button:
                if user_email and subject and body:
                    try:
                        # Construct the email message
                        total_body = f"Message from: {user_email}\n\n{body}"
                        msg = MIMEText(total_body)
                        msg['From'] = email_sender
                        msg['To'] = email_receiver
                        msg['Subject'] = subject

                        # Send the email
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        # NOTE: You must have secrets configured in Streamlit Cloud for this to work.
                        # The secrets should look like: [email] gmail = "your_email@gmail.com" password = "your_app_password"
                        server.login(st.secrets["email"]["gmail"], st.secrets["email"]["password"])
                        server.sendmail(email_sender, email_receiver, msg.as_string())
                        server.quit()
                
                        st.success('Email sent successfully! 🚀')
                    except Exception as e:
                        st.error(f"Failed to send email: {e}")
                else:
                    st.warning("Please fill out all fields.")

line(6, "blue")

# --- FOOTER ---
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h4 style='text-align: center; color: white;'>Website built with Streamlit</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: lightblue;'>Programmed in Python</h4>", unsafe_allow_html=True)
    with col2:
        _, col_img1, _, col_img2, _ = st.columns(5)
        with col_img1:
            centrar_imagen("https://i.postimg.cc/cJhYJnqx/streamlit-logo.jpg", width=100)
        with col_img2:
            centrar_imagen("https://i.postimg.cc/9Q3yg2th/python.png", width=100)

line(6, "blue")







