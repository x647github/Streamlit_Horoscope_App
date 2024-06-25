import streamlit as st
from common.utils import return_horoscope, display

st.set_page_config(page_title='Leo', page_icon=':leo:')
st.title('Leo :leo:')
res = return_horoscope('Leo')
display(res)