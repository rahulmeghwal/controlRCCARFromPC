char data = '0';
int val = -1;

// Car movements signals from arduino
int left    = 0;
int right   = 0;
int forward = 0;
int reverse = 0;

/*
** Details : Car movement control pins
**
** Connect below output pins  to RF controller's movement pins
** i.e. connect below pins to the left,righ,forward and reverse to
** remote's respective buttons(signal triggers)
*/

const int leftTurnPin    = 4; // Output Pin
const int rightTurnPin   = 5; // Output Pin
const int reverseMovePin = 6; // Output Pin
const int forwardMovePin = 7; // Output Pin


void setup() {
  
Serial.begin(115200); // opens serial port, sets data rate to 9600 bps

// Declare signal pins as OUTPUT pins
pinMode(leftTurnPin, OUTPUT);
pinMode(rightTurnPin, OUTPUT);
pinMode(reverseMovePin, OUTPUT);
pinMode(forwardMovePin, OUTPUT);

}

void loop() {

    // read from serial while data is available
    while(Serial.available()){
      data = Serial.read();        
    }

    // convert to int 
    // value sent from keyboard is = 65 + (a combination of 4 bits )
    val = data - 65 ;

    // each bit of represents the button pressed on keyboard
    reverse = val & 1<<0;
    forward = val & 1<<1;
    right   = val & 1<<2;
    left    = val & 1<<3;

    // Write to arduino outpins the signals recieved from keyboard 
    // My RF controller worked on active low pins, hence I had to invert the signals
    
    digitalWrite(leftTurnPin, !left);
    digitalWrite(rightTurnPin, !right);
    digitalWrite(reverseMovePin, !reverse);
    digitalWrite(forwardMovePin, !forward);
         
}
