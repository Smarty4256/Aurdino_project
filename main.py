from fastapi import FastAPI
# import serial
# import time

app = FastAPI()

# arduino = serial.Serial('COM7', 9600)  # change COM
# time.sleep(1)

@app.get("/")
def home():
    return {"msg": "API running"}
@app.get("/on")
def led_on():
    return {"status": "ON"}
@app.get("/off")
def led_off():
    return {"status": "OFF"}

