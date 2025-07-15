import board, time, busio, asyncio, threading
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import justpy as jp
from gpiozero import LED
import param
import init

# print pH on the terminal
async def print_ph():
    while True:
        ph = init.getPh("A0")
        print("pH:", ph)
        await asyncio.sleep(1)
