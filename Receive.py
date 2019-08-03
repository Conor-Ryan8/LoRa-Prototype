import serial
import time
from datetime import datetime
import RPi.GPIO as GPIO
Counter = 1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
Buzzer = GPIO.PWM(23,2500)

Radio = serial.Serial(
    
    port='/dev/ttyS0',
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

def SetBand():
    
    print('Setting Band to 865.2MHz')
    Radio.write('AT+BAND=865200000\r\n'.encode())
    Reply = Radio.read(10)
    time.sleep(0.5)
    if 'OK'.encode() in Reply:
        print('Band set to 865.2MHz')
    else:
        print('Band set Error!.....')

SetBand()
print('Listening...')

while(1):      
    Received = Radio.read(100)
    Received = Received.decode()   
    if "RCV" in Received:     
        
        try:
            x, Data = Received.split('=')
            Address,Length,Data,RSSI,SNR = Data.split(',')
            SNR = int(SNR)
            Now = datetime.now()
            Timestamp, Nanoseconds = str(Now).split('.')
            Date, Timestamp = Timestamp.split(' ')
            GPIO.output(18,GPIO.HIGH)
            print('------------ Packet No:',Counter,' -------------')
            print('Data Received at',Timestamp)
            print('Address:',Address)
            print('Length:',Length)
            print('Data:',Data)
            print('Received Signal Strength Indicator:',RSSI)
            print('Signal to Noise Ratio:',SNR)
            print('________________________________________')
            Counter += 1
            Buzzer.start(1)
            time.sleep(0.05)
            Buzzer.stop(1)
            time.sleep(0.2)
            GPIO.output(18,GPIO.LOW)
            
        
        except:
            print('Read Error')
