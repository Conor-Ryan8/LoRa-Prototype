#define LED 2
String Send = "AT+SEND=";
int Address = 0;
int PayloadLength = 4; 
String Data = "Test"; 

void setup()
{
    Serial.begin(115200);
    delay(100);
    Serial.print("AT+BAND=865200000\r\n");
    delay(100);
    Serial.print("AT+ADDRESS=1\r\n");
    delay(100);
    pinMode(LED,OUTPUT);    
}
void loop()
{    
    String Packet = Send + Address + ',' + PayloadLength + ',' + Data; 
    Serial.println(Packet);    
    digitalWrite(LED,HIGH);
    delay(100);
    digitalWrite(LED, LOW);
    delay(3000);
}
