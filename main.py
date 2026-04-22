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
    arduino.write(b'1')
    return {"status": "ON"}

@app.get("/off")
def led_off():
    arduino.write(b'0')
    return {"status": "OFF"}

