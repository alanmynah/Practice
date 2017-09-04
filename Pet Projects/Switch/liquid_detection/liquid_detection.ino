int liquid = 7;

int liquid_level = 0;

void setup() {
  Serial.begin(9600);
  pinMode(liquid, INPUT); 
}

void loop() {
  liquid_level = digitalRead(liquid);
  if (liquid_level == 1)
  {
    Serial.println("TEA");
  }
  else 
  {
    Serial.println("Nothing");
  }
  //Serial.print("Liquid level = ");
  //Serial.println(liquid_level, DEC);
  delay(1000);
}

