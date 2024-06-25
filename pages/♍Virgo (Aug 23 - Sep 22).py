import streamlit as st
from common.utils import return_horoscope, display

st.set_page_config(page_title='Virgo', page_icon=':virgo:')
st.title('Virgo :virgo:')
res = return_horoscope('Virgo')
display(res)