import streamlit as st
from common.utils import return_horoscope, display

st.set_page_config(page_title='Scorpio', page_icon=':scorpius:')
st.title('Scorpio :scorpius:')
res = return_horoscope('Scorpio')
display(res)