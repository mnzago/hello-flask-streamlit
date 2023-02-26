import requests
import streamlit as st

API_URL = 'http://localhost:5000'
#API_URL = 'https://hello-world-app-flask.herokuapp.com/'

@st.cache(show_spinner=False)
def hello_world():
    response = requests.get(f"{API_URL}/hello/")
    #response = requests.get(f"{API_URL}")
    if response.status_code == 200:
        data = response.json()
        message = data.get('message', 'Unknown message')
    else:
        message = 'Failed to get message from API'
    
    return(message)

msg=hello_world()
st.write(msg)