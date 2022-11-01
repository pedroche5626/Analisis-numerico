int fotoIz = A0; //Establecer pin A0 para fotorecistencia
int fotoDe = A1;
int IntIz = 0;
int IntDe = 0;


void setup()
{
 
  pinMode (A0,INPUT);  //Establecer pin como entrada
  pinMode (A1, INPUT);
  Serial.begin(9600);
  Serial.println("FotoIzquierda, FotoDerecha/100");
  Serial.println(120);
}

void loop()
{
  fotoIz = analogRead(fotoIz);
  fotoDe = analogRead(fotoDe);
  //fotoIz = random(95,100);
  //fotoDe = random(95,100);
  
  Serial.println(fotoIz);
  Serial.print(" ");
  Serial.println(fotoDe);
  delay(100);
  
  
 
  
}
