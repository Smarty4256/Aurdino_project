import streamlit as st
import requests

API = "http://localhost:8000"

st.title("💡 LED Control")

if st.button("ON"):
    requests.get(f"{API}/on")
    st.success("LED ON")

if st.button("OFF"):
    requests.get(f"{API}/off")
    st.error("LED OFF")