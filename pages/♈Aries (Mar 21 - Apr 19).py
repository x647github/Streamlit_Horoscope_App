import streamlit as st
from common.utils import return_horoscope, display

st.set_page_config(page_title='Aries', page_icon=':aries:')
st.title('Aries :aries:')
res = return_horoscope('Aries')
display(res)