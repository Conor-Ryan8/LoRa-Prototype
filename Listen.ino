#define ledPin 2
String incomingString;

void setup()
{
    Serial.begin(115200);
    Serial.print("AT+BAND=865200000\r\n");
    delay(20);
    pinMode(ledPin,OUTPUT);
}

void loop()
{
    if (Serial.available())
    {
        incomingString = Serial.readString();
        digitalWrite(ledPin,HIGH);
        delay(200);
        digitalWrite(ledPin,LOW);
    }
}
