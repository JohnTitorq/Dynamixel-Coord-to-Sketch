#include <Dynamixel2Arduino.h>
#define DXL_SERIAL Serial3
#define DEBUG_SERIAL Serial 

#define NServos = 6; // SPECIFY THE NUMBER OF SERVO DRIVES

const uint8_t DXL_DIR_PIN = 22; 
const float DXL_PROTOCOL_VERSION = 1.0;

Dynamixel2Arduino dxl(DXL_SERIAL, DXL_DIR_PIN); 

void setup() {

  DEBUG_SERIAL.begin(57600); 
  dxl.begin(1000000); 
  dxl.setPortProtocolVersion(DXL_PROTOCOL_VERSION);
  for (x = 1; x < NServos + 1; x++) { dxl.setOperatingMode( x, OP_POSITION ) }

  /*
  dxl.setOperatingMode(1, OP_POSITION);
  dxl.setOperatingMode(2, OP_POSITION); 
  dxl.setOperatingMode(3, OP_POSITION);
  dxl.setOperatingMode(4, OP_POSITION);
  dxl.setOperatingMode(5, OP_POSITION);
  dxl.setOperatingMode(6, OP_POSITION);
  */
}

void loop() {
  
  // paste code from the program here 
}

void Dynamixel_Gear(int _id, int _velocity, int _position, int _delay) {
  
  dxl.setGoalVelocity(_id, _velocity);
  dxl.setGoalPosition(_id, _position);
  delay(_delay);
}

    
