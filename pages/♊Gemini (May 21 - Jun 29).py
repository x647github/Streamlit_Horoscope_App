import streamlit as st
from common.utils import return_horoscope, display

st.set_page_config(page_title='Gemini', page_icon=':gemini:')
st.title('Gemini :gemini:')
res = return_horoscope('Gemini')
display(res)