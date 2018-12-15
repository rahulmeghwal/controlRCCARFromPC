char incomingByte = '0';
char data = '0';
int val = -1;
char first = '0';
int iter = 0;
char State = 'X';

// Car movements 
int left = 0;
int right = 0;
int forward = 0;
int reverse = 0;

// car movement control pins
const int leftTurnPin = 4; // Output Pin
const int rightTurnPin = 5; // Output Pin
const int forwardMovePin = 6; // Output Pin
const int reverseMovePin = 7; // Output Pin


void setup() {
  
Serial.begin(115200); // opens serial port, sets data rate to 9600 bps

pinMode(leftTurnPin, OUTPUT);
pinMode(rightTurnPin, OUTPUT);
pinMode(forwardMovePin, OUTPUT);
pinMode(reverseMovePin, OUTPUT);

}

void loop() {

    incomingByte = '0';
    
    while(Serial.available()){
      data = Serial.read();        
    }

    // convert to 
    val = data - 65 ;

    reverse = val & 1<<0;
    forward = val & 1<<1;
    right   = val & 1<<2;
    left    = val & 1<<3;

    digitalWrite(leftTurnPin, left);
    digitalWrite(rightTurnPin, right);
    digitalWrite(forwardMovePin, forward);
    digitalWrite(reverseMovePin, reverse);
         
}
