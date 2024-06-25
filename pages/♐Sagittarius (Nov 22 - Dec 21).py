import streamlit as st
from common.utils import return_horoscope, display

st.set_page_config(page_title='Sagittarius', page_icon=':sagittarius:')
st.title('Sagittarius :sagittarius:')
res = return_horoscope('Sagittarius')
display(res)