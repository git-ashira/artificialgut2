import board, time, busio, asyncio, threading
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import justpy as jp
from gpiozero import LED

# initialize the I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# create the ADC object, add more ads channels after we recieve them, just change the address

ads1 = ADS.ADS1115(i2c, address=0x48) #for probes 1-4
ads2 = ADS.ADS1115(i2c, address=0x49) # check the probes (not recieved)

# create the analog input channel 
channel1 = AnalogIn(ads1, ADS.P0) #channel for probe 1

# get voltages
volt1 = channel1.voltage

# convert voltage to pH
def voltage_to_ph(voltage):
    return 7 - 5.98 * (voltage - 2.5)   

# get pH value
ph1 = voltage_to_ph(volt1)



# define GPIO pins for pumps
pump_pins = {
    "pump1": 17,
    "pump2": 27,
    "pump3": 22,
    "pump4": 23
}
# create LED objects for pumps
pumps = {name: LED(pin) for name, pin in pump_pins.items()} 