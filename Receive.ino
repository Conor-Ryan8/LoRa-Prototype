#define LED 2
#define Buzzer 9
String Incoming;

void setup()
{
    Serial.begin(115200);
    Serial.print("AT+BAND=865200000\r\n");
    delay(20);
    pinMode(LED,OUTPUT);
    pinMode(Buzzer, OUTPUT);
}
void loop()
{
    if (Serial.available())
    {
        Incoming = Serial.readString();
        digitalWrite(LED,HIGH);
        tone(Buzzer, 1000);
        delay(200);
        digitalWrite(LED,LOW);
        noTone(Buzzer);      
    }
}
