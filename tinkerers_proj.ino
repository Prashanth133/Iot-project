int Flamepin = 11;
int Smokepin = 10;
int sensePin = A1;  
int sensorInput;    
double temp;        
 
void setup() {
  // put your setup code here, to run once:
  //Start the Serial Port at 9600 baud (default)
  pinMode(Flamepin,INPUT);
  pinMode(Smokepin,INPUT);
  
   Serial.begin(9600);
}
void loop() {
  // put your main code here, to run repeatedly: 
  sensorInput = analogRead(A1);    
  temp = (double)sensorInput / 1024;      
  temp = temp * 5;                 
  temp = (temp - 0.5)*100;                
  Serial.print(temp);
  Serial.print(",");
 
  int Flame = digitalRead(Flamepin);
  
if(Flame == HIGH)
{
  Serial.print(1);
  Serial.print(",");
}
else
{
 Serial.print(0);
 Serial.print(",");
}
int Smoke = digitalRead(Smokepin);

if(Smoke == HIGH)
{
  Serial.print(1);
  Serial.println();
}
else
{
 Serial.print(0);
 Serial.println();
}
  delay(300);
}
