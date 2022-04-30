# Sven Wille ETS2021
# 30.04.2022
# IDUINO Water Sensor(SE045)

from machine import Pin, ADC        # Pin und ADC (analog Pin) importieren
from time import sleep              # sleep importieren

analog_Pin = ADC(Pin(33))           # Analog Pin 33 
analog_Pin.atten(ADC.ATTN_11DB)     # 3.3V Spannungsbereich 

while True:
  water_value = analog_Pin.read()   # Analogwert auslesen
  print(water_value)                # Analogwer ausgeben
  sleep(0.5)