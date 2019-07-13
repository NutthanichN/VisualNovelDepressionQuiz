import network
import urequests
import json
from machine import ADC,Pin
from time import sleep
import math
from _thread import start_new_thread as thread

beat = ADC(Pin(32))
beat.atten(ADC.ATTN_11DB)

messure_time = 5
messure_sleep = 0.02
messure_loop = int(messure_time//messure_sleep)

ssid = 'exceed16_6'
pwd = '12345678'
station = network.WLAN(network.STA_IF)
station.active(True)

url = "https://exceed.superposition.pknn.dev/data/group_one"
data = {"Temp": 0.00, "HeartRate":0.00}
headers = {"content-type":"application/json"}

#-------#

RawADC = ADC(Pin(34))
RawADC.atten(ADC.ATTN_11DB)

def Thermistor(RawADC) :

  Temp = math.log(abs(100000.0*((4095.0/RawADC-1))),10)
  Temp = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 *  Temp * Temp ))* Temp )
  Temp = Temp - 293.15 # Convert Kelvin to Celcius
  #Temp = (Temp * 9.0)/ 5.0 + 32.0 # Convert Celcius to Fahrenheit
  return Temp
  
def temp() :
  while(1) :
    readVal = RawADC.read() * 3.3 / 4095
    tem = Thermistor(readVal)
    return tem # display tempature
    #//Serial.println(readVal); // display tempature
    sleep(0.2)
    #----#

def heartbeat() :
  while True:
    data = [100 for _ in range(messure_loop)]

    data_sum = 0

    i = 0
    while i < messure_loop:
      rawValue = beat.read() #* 5 / 1023
      data[i] = rawValue
      data_sum += rawValue
      sleep(messure_sleep)
      i += 1

    average = data_sum/messure_loop
    thres = average*1.06

    beatCount = 0

    for i, raw in enumerate(data):
      if i == 0:
        continue
      if raw>=thres and data[i-1] < thres:
        beatCount += 1
        
    bpm = beatCount*60/messure_time

    #print("BPM:",bpm)
    return bpm
    #-----#

def net() :
  while(1):
    while not station.isconnected():
      station.connect(ssid, pwd)
      print("Connecting...")
      sleep(1)
      if station.isconnected():
        print("Connected")
    
    js = json.dumps({"data": data})
    r = urequests.post(url, data=js, headers=headers)
    results = r.json()
    print(results)
    #print(temp)
    #data["temp"] += 1
    data["HeartRate"] = heartbeat()
    data["Temp"] = temp()
    sleep(4)
    #net
 
thread(net,())
thread(heartbeat,())
thread(temp,())
