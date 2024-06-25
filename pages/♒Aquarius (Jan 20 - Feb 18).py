import streamlit as st
from common.utils import return_horoscope, display

st.set_page_config(page_title='Aquarius', page_icon=':aquarius:')
st.title('Aquarius :aquarius:')
res = return_horoscope('Aquarius')
display(res)