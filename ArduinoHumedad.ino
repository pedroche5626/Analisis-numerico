#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT11
 
// Inicializamos el sensor DHT11
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  // Comenzamos el sensor DHT
  dht.begin();
}

void loop() {
  
  // put your main code here, to run repeatedly:
  delay(5000);
  
  // Humedad relativa
  float humedad = dht.readHumidity();
  // Temperatura en grados 
  float temperatura = dht.readTemperature();
 
  Serial.print("Humedad: ");
  Serial.println(humedad);
 
  Serial.print("Temperatura: ");
  Serial.println(temperatura);
}
