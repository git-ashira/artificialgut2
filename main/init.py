import board, time, busio, asyncio, threading
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import justpy as jp
from gpiozero import LED
import param

# convert voltage to pH
def voltage_to_ph(voltage, ph_m, ph_off):
    value = (7.0 - (2.5 - voltage) * ph_m) + ph_off
    return value

# get ph reading from the probe
def getPh(Probe):

    # Get the pin, channel, m and offset for the specified probe
    pin = param.get_ph_pins(Probe)
    channel = AnalogIn(pin)
    volt = channel.voltage
    ph_m = param.get_ph_m(Probe)
    ph_off = param.get_ph_off(Probe)

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

