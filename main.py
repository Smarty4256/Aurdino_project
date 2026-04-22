from fastapi import FastAPI

app = FastAPI()

latest_command = "OFF"

@app.get("/")
def home():
    return {"msg": "API running"}

@app.get("/on")
def led_on():
    global latest_command
    latest_command = "ON"
    return {"status": "ON"}

@app.get("/off")
def led_off():
    global latest_command
    latest_command = "OFF"
    return {"status": "OFF"}

@app.get("/status")
def get_status():
    return {"command": latest_command}