import board, time, busio, asyncio, threading
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import init
from dataclasses import dataclass

@dataclass
class pH_m_values:
    A0: float = -5.98
    A1: float = -6.00
    A2: float = -6.02
    A3: float = -6.04
    A4: float = -6.06
    A5: float = -6.08

@dataclass
class pH_off_values:
    A0: float = 0.1
    A1: float = 0.1
    A2: float = 0.1
    A3: float = 0.1
    A4: float = 0.1
    A5: float = 0.1

@dataclass
class PumpPins:
    C0A: int = 17
    C0B: int = 27
    C0F: int = 23
    C1F: int = 24






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
# ads2 = ADS.ADS1115(i2c, address=0x49) # check the probes (not recieved)

def get_ph_pins():
    return {
        "A0": (aqds1, AqDS.P0),
        # "A1": (ads1, ADS.P1),
        # "A2": (ads1, ADS.P2),
        # "A3": (ads1, ADS.P3),
    }



# convert voltage to pH
def voltage_to_ph(voltage, ph_m, ph_off):
    value = (7.0 - (2.5 - voltage) * ph_m) + ph_off
    return value

# get ph reading from the probe
def getPh(Probe):

    # Get the pin, channel, m and offset for the specified probe
    
    pin = get_ph_pins()
    channel = AnalogIn(*pin[Probe]) # changed this line to unpack the tuple
    volt = channel.voltage
    m = get_ph_m()
    ph_m = m[Probe]
    off = get_ph_off()
    ph_off = off[Probe]

    buf = [0] * 10
    
    # Take 10 readings from the pH sensor
    for i in range(10):
        buf[i] = volt  # Assuming analog_read is defined elsewhere
        time.sleep(0.01)  # 10ms delay
    
     # Sort readings from small to large (bubble sort)
    for i in range(9):
        for j in range(i + 1, 10):
            if buf[i] > buf[j]:
                buf[i], buf[j] = buf[j], buf[i]

    # Calculate average of middle 6 readings
    avg_value = sum(buf[2:8]) / 6.0

    # convert into pH

    ph = voltage_to_ph(avg_value, ph_m, ph_off)

    return ph



def new_function(a):
    # This function is a placeholder for any new functionality you want to add
    
    pnass = get_pump_pins()
    Print = pnass[*a]

new_function("C0A")