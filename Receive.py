import serial
import time
from datetime import datetime
Counter = 1

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
            print('------------ Packet No:',Counter,' -------------')
            print('Data Received at',Timestamp)
            print('Address:',Address)
            print('Length:',Length)
            print('Data:',Data)
            print('Received Signal Strength Indicator:',RSSI)
            print('Signal to Noise Ratio:',SNR)
            print('________________________________________')
            Counter += 1
        
        except:
            print('Read Error')
