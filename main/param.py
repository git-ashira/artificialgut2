import board, time, busio, asyncio, threading
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import init

def get_ph_m():
    return {
        "A0": -5.98,
        "A1": -6.00,
        "A2": -6.02,
        "A3": -6.04,
        "A4": -6.06,
        "A5": -6.08,
    }

def get_ph_off():
    return {
        "A0": 0.1,
        "A1": 0.1,
        "A2": 0.1,
        "A3": 0.1,
        "A4": 0.1,
        "A5": 0.1,
    }


def get_pump_pins():
    return {
        "C0A": 17,
        "C0B": 27,
        "C0F": 23,
        "C1F": 24,
    }


# initialize the I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# create the ADC object, add more ads channels after we recieve them, just change the address

ads1 = ADS.ADS1115(i2c, address=0x48) #for probes 1-4
ads2 = ADS.ADS1115(i2c, address=0x49) # check the probes (not recieved)

def get_ph_pins():
    return {
        "A0": (ads1, ADS.P0),
        "A1": (ads1, ADS.P1),
        "A2": (ads1, ADS.P2),
        "A3": (ads1, ADS.P3),
    }


