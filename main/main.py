import board, time, busio, asyncio, threading
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import justpy as jp
import gpiozero
import param
import init

# print pH on the terminal
while True:
    h = param.get_ph_pins()
    ph = h["A0"]
    print("pH:", ph)
    asyncio.sleep(1000)

