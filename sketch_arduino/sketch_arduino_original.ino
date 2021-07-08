void setup() {
   pinMode(PD2, INPUT_PULLUP);
   pinMode(PD3, INPUT_PULLUP);
   pinMode(PD4, OUTPUT);
   pinMode(PD5, OUTPUT);
}

void loop() {
  if(digitalRead(PD2) == LOW){
    digitalWrite(PD4, HIGH);
  }
  else{ 
    digitalWrite(PD4, LOW);
  }

  if(digitalRead(PD3) == LOW){
    digitalWrite(PD5, HIGH);
  } else {
    digitalWrite(PD5, LOW); 
  }
}
