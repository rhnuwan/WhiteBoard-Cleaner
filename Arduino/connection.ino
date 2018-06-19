int inPin = 7;
int outPin = 13;
int data = 0;
void setup() 
{
  pinMode(inPin, INPUT);
  pinMode(outPin,OUTPUT);
  Serial.begin(9600);

}

void loop() 
{
  if(digitalRead(inPin) == 'HIGH'){
    Serial.println('s');
    delay(100);

	}

	if(Serial.available()){
		data = Serial.read();
		if(data == '1'){
			digitalWrite(outPin, HIGH);
			delay(1000);
		}
	}
}
