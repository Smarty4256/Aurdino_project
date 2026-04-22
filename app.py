import streamlit as st
import requests

st.set_page_config(
    page_title="Sheshu IoT Control 🚀",
    page_icon="💡"
)

API = "https://aurdino-project.onrender.com"

st.title("💡 Sheshu Smart Home Control")
st.caption("Control your devices from anywhere 🌍")

if st.button("Turn ON"):
    res = requests.get(f"{API}/on")
    st.success(res.json()["status"])

if st.button("Turn OFF"):
    res = requests.get(f"{API}/off")
    st.error(res.json()["status"])