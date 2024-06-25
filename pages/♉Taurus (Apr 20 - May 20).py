import streamlit as st
from common.utils import return_horoscope, display

st.set_page_config(page_title='Taurus', page_icon=':taurus:')
st.title('Taurus :taurus:')
res = return_horoscope('Taurus')
display(res)