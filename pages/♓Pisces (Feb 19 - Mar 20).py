import streamlit as st
from common.utils import return_horoscope, display

st.set_page_config(page_title='Pisces', page_icon=':pisces:')
st.title('Pisces :pisces:')
res = return_horoscope('Pisces')
display(res)