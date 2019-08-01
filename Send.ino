#define ledPin 2

void setup()
{
    Serial.begin(115200); 
    Serial.print("AT+BAND=865200000\r\n");
    pinMode(ledPin,OUTPUT);
}

void loop()
{
    Serial.println("AT+SEND=0,8,Testing!\r\n");
    digitalWrite(ledPin,HIGH);
    delay(200);
    digitalWrite(ledPin, LOW);
    delay(5000);
}
