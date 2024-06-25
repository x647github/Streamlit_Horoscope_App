import streamlit as st

st.set_page_config(page_title='Horoscope', page_icon='🔮')
st.title('🔮 Horoscope App')

expander_bar = st.expander('About')
expander_bar.markdown('''
    **Horoscope source:** [horoscope.com](https://www.horoscope.com/us).
''')

st.subheader('Welcome to the Horoscope App')
st.markdown('👈 **Choose your zodiac sign** to find your daily and weekly horoscopes.')
st.image('./img.jpg')
