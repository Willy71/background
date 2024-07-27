import streamlit as st

from streamlit_gtag import st_gtag

st.set_page_config(
    page_title="Google Gtag",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Google Analytics :chart:")

# Este codigo es el mejor de los tres por que fuciona directamente si se carga la pagina principal
st_gtag(
    key="gtag_send_event_page_load",
    id="G-ZY2745B9DJ",
    event_name="app_main_page_load",
    params={
        "event_category": "page_load",
        "event_label": "main_page",
        "value": 1,
    },
)

st_gtag(
    key="gtag_send_event_a",
    id="G-LDSKH1L6V2",
    event_name="app_main_page",
    params={
        "event_category": "test_category_a",
        "event_label": "test_label_a",
        "value": 97,
    },
)

if st.button("Send Event A"):
    st_gtag(
        key="gtag_send_event_b",
        id="G-LDSKH1L6V2",
        event_name="send_event_button",
        params={
            "event_category": "test_category_b",
            "event_label": "test_label_b",
            "value": 97,
        },
    )



