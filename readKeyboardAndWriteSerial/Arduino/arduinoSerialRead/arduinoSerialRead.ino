char data = '0';
int val = -1;

// Car movements 
int left = 0;
int right = 0;
int forward = 0;
int reverse = 0;

// car movement control pins
const int leftTurnPin = 4; // Output Pin
const int rightTurnPin = 5; // Output Pin
const int reverseMovePin = 6; // Output Pin
const int forwardMovePin = 7; // Output Pin


void setup() {
  
Serial.begin(115200); // opens serial port, sets data rate to 9600 bps

pinMode(leftTurnPin, OUTPUT);
pinMode(rightTurnPin, OUTPUT);
pinMode(reverseMovePin, OUTPUT);
pinMode(forwardMovePin, OUTPUT);

}

void loop() {

    while(Serial.available()){
      data = Serial.read();        
    }

    // convert to int
    val = data - 65 ;

    reverse = val & 1<<0;
    forward = val & 1<<1;
    right   = val & 1<<2;
    left    = val & 1<<3;

    digitalWrite(leftTurnPin, !left);
    digitalWrite(rightTurnPin, !right);
    digitalWrite(reverseMovePin, !reverse);
    digitalWrite(forwardMovePin, !forward);
         
}
