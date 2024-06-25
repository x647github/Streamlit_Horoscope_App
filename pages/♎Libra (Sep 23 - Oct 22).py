import streamlit as st
from common.utils import return_horoscope, display

st.set_page_config(page_title='Libra', page_icon=':libra:')
st.title('Libra :libra:')
res = return_horoscope('Libra')
display(res)