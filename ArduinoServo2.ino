#include <Servo.h> 
 
Servo myservo;  //creamos un objeto servo 


void setup() {
  myservo.attach(3);  // asignamos el pin 3 al servo.

  // put your setup code here, to run once:
    Serial.begin(9600);
   

}

void loop() {
  // put your main code here, to run repeatedly:
  
   if(Serial.available() > 0 ){
	 String teststr = Serial.readString(); 
         int  angulo = teststr.toInt();
         myservo.write(angulo);    
	 delay(10);     
  }
}
