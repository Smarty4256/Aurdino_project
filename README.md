# 💡 Arduino LED Control using FastAPI + Streamlit

## 👨‍💻 Author

**Sheshu gandhasiri**

---

## 🚀 Project Overview

This project allows you to control an LED connected to Arduino using a web interface.

You can:

* 📱 Control from mobile
* 💻 Control from laptop
* 🌐 Access via browser
* ⚡ Use FastAPI as backend

---

## 🧠 Architecture

Phone / Laptop → Streamlit UI → FastAPI → Serial (USB) → Arduino → LED

---

## 🛠️ Tech Stack

* Python 🐍
* FastAPI
* Streamlit
* PySerial
* Arduino (C++)

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Smarty4256/Aurdino_project.git
cd Aurdino_project
```

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Start FastAPI backend

```bash
uvicorn main:app --reload
```

### Start Streamlit frontend

```bash
streamlit run app.py
```

---

## 🔌 Arduino Setup

* Connect LED to Arduino (with resistor)
* Upload Arduino serial code
* Ensure correct COM port in Python

---

## 📱 Access

* Local: http://localhost:8501
* Same WiFi: http://<your-ip>:8501
* Global: Use ngrok

---

## 🔥 Features

* Remote LED control
* Works across devices
* Real-time communication
* Simple IoT system

---

## 🚧 Future Improvements

* 🔌 Control Relay Module to switch real household AC appliances (bulb, fan, etc.)
* 🏠 Extend system for home automation (multiple devices control)
* 🍓 Upgrade to Raspberry Pi for always-on local server (remove laptop dependency)
* 🌐 Deploy backend to cloud (AWS / Azure) for global access without ngrok
* 🔐 Add authentication & security (login system, API protection)
* 📊 Add dashboard for monitoring device status
* 📡 Integrate ESP32 for wireless communication (no USB needed)




---

## ⭐ If you like this project

Give it a star on GitHub ⭐
