import streamlit as st
from common.utils import return_horoscope, display

st.set_page_config(page_title='Capricorn', page_icon=':capricorn:')
st.title('Capricorn :capricorn:')
res = return_horoscope('Capricorn')
display(res)