import serial
import time
from datetime import datetime
import RPi.GPIO as GPIO
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
Status = 0

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
        print('Band Error!.....')

def SendSignals():
    global Status   
    while True:        
        if Status == 1:
            Now = datetime.now()
            Timestamp, x = str(Now).split('.')
            x, Timestamp = Timestamp.split(' ')
            print('Sending Test Signal at',Timestamp)
            Radio.write('AT+SEND=0,4,Test\r\n'.encode())
            Reply = Radio.read(10)            
            if 'OK'.encode() in Reply:           
                GPIO.output(18,GPIO.HIGH)
                Now = datetime.now()
                Timestamp, x = str(Now).split('.')
                x, Timestamp = Timestamp.split(' ')
                print('Signal Sent at',Timestamp)
                time.sleep(0.2)
                GPIO.output(18,GPIO.LOW)                
            else:          
                print('Send Error!.....')           
            time.sleep(5)      
SetBand()
Signals = threading.Thread(target=SendSignals)
Signals.start()

while True:    
    button_state = GPIO.input(23)   
    if button_state == False:        
        if Status == 0:           
            Status = 1
            print('Starting Tests...')        
        else:           
            Status = 0
            print('Stopping Tests...')       
        time.sleep(1)  
