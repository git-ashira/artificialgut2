import board, time, busio, asyncio, threading
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import justpy as jp
import gpiozero
import param
import init


def new_function(a):
    # This function is a placeholder for any new functionality you want to add
    
    pnass = param.get_pump_pins()
    Print = pnass[*a]

new_function("C0A")
