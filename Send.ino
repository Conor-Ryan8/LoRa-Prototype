#define LED 2

void setup()
{
    Serial.begin(115200); 
    Serial.print("AT+BAND=865200000\r\n");
    pinMode(LED,OUTPUT);
}

void loop()
{
    Serial.println("AT+SEND=0,4,Test\r\n");
    digitalWrite(LED,HIGH);
    delay(200);
    digitalWrite(LED, LOW);
    delay(5000);
}
