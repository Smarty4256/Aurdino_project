import streamlit as st
import requests

# 🔥 USE YOUR RENDER BACKEND URL
API = "https://aurdino-project.onrender.com"

st.title("💡 LED Control")

if st.button("ON"):
    res = requests.get(f"{API}/on")
    st.success(res.json()["status"])

if st.button("OFF"):
    res = requests.get(f"{API}/off")
    st.error(res.json()["status"])