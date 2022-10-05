
long SensorHumedad;

void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600);
}
void loop() {

  
  // put your main code here, to run repeatedly:
    SensorHumedad = random(1,100);
   
 
    Serial.print("{\"Sensor\":\"Humedad\",\"Valor\":");
    Serial.print(SensorHumedad);
    Serial.print(",\"Timestamp\":");
    Serial.print(millis());
    Serial.println("}");

    
  
  delay(20000);
}
