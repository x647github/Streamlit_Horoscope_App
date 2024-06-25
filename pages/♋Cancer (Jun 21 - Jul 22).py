import streamlit as st
from common.utils import return_horoscope, display

st.set_page_config(page_title='Cancer', page_icon=':cancer:')
st.title('Cancer :cancer:')
res = return_horoscope('Cancer')
display(res)