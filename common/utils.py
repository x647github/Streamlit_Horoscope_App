import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

@st.cache_data(show_spinner=False)
def return_horoscope(zodiac):
    url = 'https://www.horoscope.com/us'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find('section', class_='choose-zodiac')
        
    today_url = url[:-3] + data.find('h3', string=zodiac).find_parent('a')['href']
    response = requests.get(today_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    today_data = soup.find_all('p')[0].text.split('-')
    today_date, today_text = today_data[0], ''.join(today_data[1:])
    today_text = re.sub(r'(?<!\s)\.(?=\w)', '. ', today_text)
    
    tomorrow_url = today_url.replace('today', 'tomorrow')
    response = requests.get(tomorrow_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    tmr_data = soup.find_all('p')[0].text.split('-')
    tmr_date, tmr_text = tmr_data[0], ''.join(tmr_data[1:])
    tmr_text = re.sub(r'(?<!\s)\.(?=\w)', '. ', tmr_text)
    
    weekly_url = re.sub(r'-?daily', '', today_url).replace('today', 'weekly')
    response = requests.get(weekly_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    weekly_data = soup.find_all('p')[0].text.split('-')
    weekly_date, weekly_text = weekly_data[:2], ''.join(weekly_data[2:])
    weekly_text = re.sub(r'(?<!\s)\.(?=\w)', '. ', weekly_text)
    
    return today_date, today_text, tmr_date, tmr_text, weekly_date, weekly_text


def display(res):
    today_date, today_text = res[0], res[1]
    tmr_date, tmr_text = res[2], res[3]
    weekly_date, weekly_text = res[4], res[5]

    st.subheader('Today - ' + today_date)
    st.markdown(today_text)

    st.subheader('Tomorrow - ' + tmr_date)
    st.markdown(tmr_text)

    st.subheader('Weekly - ' + '-'.join(weekly_date))
    st.markdown(weekly_text)
