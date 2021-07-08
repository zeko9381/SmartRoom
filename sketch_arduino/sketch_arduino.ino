// Pin macros
#define lightSwitchPin PD2
#define doorSensorPin PD3
#define lightOutputPin PD4
#define doorOutputPin PD5

// Outputs
int lightOutputState = LOW;
int doorOutputState = LOW;

// Inputs
int lastLightState = LOW;
int lastDoorState = LOW;

// For debounce
unsigned long lightLastDebounceTime = 0;
unsigned long doorLastDebounceTime = 0;
unsigned long debounceDelay = 10;

void setup() {
  pinMode(lightSwitchPin, INPUT_PULLUP);
  pinMode(doorSensorPin, INPUT_PULLUP);
  pinMode(lightOutputPin, OUTPUT);
  pinMode(doorOutputPin, OUTPUT);

  digitalWrite(lightOutputPin, LOW);
}

void loop() {
  // Reads and saves pin states
  int lightState = digitalRead(lightSwitchPin);
  int doorState = digitalRead(doorSensorPin);

  // Checks if the state changed from the last cycle
  if(lightState != lastLightState)
    lightLastDebounceTime = millis();
  if(doorState != lastLightState)
    doorLastDebounceTime = millis();

  // If the input states lasted longer than the debounce delay, they write to the output pins
  if((millis() - lightLastDebounceTime) > debounceDelay)
    digitalWrite(lightOutputPin, lightState);
  if((millis() - doorLastDebounceTime) > debounceDelay)
     digitalWrite(doorOutputPin, doorState);  

  // Saves input states to compare if it changes in the next cycle
  lastLightState = lightState;
  lastDoorState = doorState;
}
