/*
 * Cardboard Robot with LED Matrix Drawing
 * Arduino Code for Mechanical Movement and LED Display
 * 
 * Features:
 * - Servo motor control for movement
 * - 8x8 LED matrix display with WS2812B
 * - Serial communication for Python control
 * - Drawing patterns and animations
 */

#include <Servo.h>
#include <FastLED.h>

// Servo motor pins
#define LEFT_SERVO_PIN 9
#define RIGHT_SERVO_PIN 10

// LED Matrix pins (WS2812B) - 16x16 matrix
#define LED_PIN 11
#define NUM_LEDS 256  // 16x16 matrix

// Servo objects - 4 servos for large robot
Servo leftServo;
Servo rightServo;
Servo frontServo;
Servo backServo;

// LED Matrix object - 16x16 matrix
CRGB leds[NUM_LEDS];

// Movement constants
#define STOP_ANGLE 90
#define FORWARD_LEFT 60
#define FORWARD_RIGHT 120
#define BACKWARD_LEFT 120
#define BACKWARD_RIGHT 60
#define TURN_LEFT_LEFT 60
#define TURN_LEFT_RIGHT 60
#define TURN_RIGHT_LEFT 120
#define TURN_RIGHT_RIGHT 120

// Movement speeds
#define SLOW_SPEED 1000
#define NORMAL_SPEED 500
#define FAST_SPEED 200

// LED Matrix patterns - 16x16 for large robot
byte smiley[16] = {
  B0000000000000000,
  B0000111111110000,
  B0011000000001100,
  B0100000000000010,
  B1000000000000001,
  B1000000000000001,
  B1000000000000001,
  B1000000000000001,
  B1000000000000001,
  B1000000000000001,
  B1000000000000001,
  B1000000000000001,
  B0100000000000010,
  B0011000000001100,
  B0000111111110000,
  B0000000000000000
};

byte heart[8] = {
  B00000000,
  B01100110,
  B11111111,
  B11111111,
  B01111110,
  B00111100,
  B00011000,
  B00000000
};

byte arrow[8] = {
  B00000000,
  B00010000,
  B00110000,
  B01111111,
  B01111111,
  B00110000,
  B00010000,
  B00000000
};

byte robot[8] = {
  B00111100,
  B01111110,
  B11000011,
  B10111101,
  B10111101,
  B11000011,
  B01111110,
  B00111100
};

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
  Serial.println("Cardboard Robot Ready!");
  
  // Initialize servos
  leftServo.attach(LEFT_SERVO_PIN);
  rightServo.attach(RIGHT_SERVO_PIN);
  
  // Initialize LED matrix
  FastLED.addLeds<WS2812B, LED_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setBrightness(50);
  FastLED.clear();
  FastLED.show();
  
  // Center servos
  leftServo.write(STOP_ANGLE);
  rightServo.write(STOP_ANGLE);
  
  // Display startup pattern
  displayPattern(robot);
  delay(2000);
  displayPattern(smiley);
  delay(1000);
  clearDisplay();
  
  Serial.println("Robot initialized. Send commands via serial:");
  Serial.println("Commands: F(forward), B(backward), L(left), R(right), S(stop)");
  Serial.println("LED: P(pattern), C(clear), H(heart), A(arrow)");
  Serial.println("Speed: 1(slow), 2(normal), 3(fast)");
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    processCommand(command);
  }
  
  // Small delay to prevent overwhelming the serial buffer
  delay(10);
}

void processCommand(char command) {
  switch (command) {
    case 'F':
      moveForward();
      break;
    case 'B':
      moveBackward();
      break;
    case 'L':
      turnLeft();
      break;
    case 'R':
      turnRight();
      break;
    case 'S':
      stopMovement();
      break;
    case 'P':
      displayPattern(smiley);
      break;
    case 'C':
      clearDisplay();
      break;
    case 'H':
      displayPattern(heart);
      break;
    case 'A':
      displayPattern(arrow);
      break;
    case '1':
      setSpeed(SLOW_SPEED);
      break;
    case '2':
      setSpeed(NORMAL_SPEED);
      break;
    case '3':
      setSpeed(FAST_SPEED);
      break;
    default:
      Serial.println("Unknown command: " + String(command));
      break;
  }
}

void moveForward() {
  Serial.println("Moving forward");
  leftServo.write(FORWARD_LEFT);
  rightServo.write(FORWARD_RIGHT);
  displayPattern(arrow);
}

void moveBackward() {
  Serial.println("Moving backward");
  leftServo.write(BACKWARD_LEFT);
  rightServo.write(BACKWARD_RIGHT);
  displayPattern(arrow);
}

void turnLeft() {
  Serial.println("Turning left");
  leftServo.write(TURN_LEFT_LEFT);
  rightServo.write(TURN_LEFT_RIGHT);
  displayPattern(arrow);
}

void turnRight() {
  Serial.println("Turning right");
  leftServo.write(TURN_RIGHT_LEFT);
  rightServo.write(TURN_RIGHT_RIGHT);
  displayPattern(arrow);
}

void stopMovement() {
  Serial.println("Stopping");
  leftServo.write(STOP_ANGLE);
  rightServo.write(STOP_ANGLE);
  displayPattern(robot);
}

void displayPattern(byte pattern[8]) {
  // Convert 8x8 pattern to 16x16 display
  for (int y = 0; y < 8; y++) {
    for (int x = 0; x < 8; x++) {
      if (pattern[y] & (0x80 >> x)) {
        // Set pixel and its mirror for 16x16 display
        int led1 = y * 16 + x;
        int led2 = y * 16 + (15 - x);
        int led3 = (15 - y) * 16 + x;
        int led4 = (15 - y) * 16 + (15 - x);
        
        if (led1 < NUM_LEDS) leds[led1] = CRGB::White;
        if (led2 < NUM_LEDS) leds[led2] = CRGB::White;
        if (led3 < NUM_LEDS) leds[led3] = CRGB::White;
        if (led4 < NUM_LEDS) leds[led4] = CRGB::White;
      }
    }
  }
  FastLED.show();
}

void clearDisplay() {
  FastLED.clear();
  FastLED.show();
}

void setSpeed(int speed) {
  // This is a placeholder for speed control
  // In a more advanced version, you could use PWM to control servo speed
  Serial.println("Speed set to: " + String(speed));
}

// Animation functions
void animateHeart() {
  for (int i = 0; i < 3; i++) {
    displayPattern(heart);
    delay(500);
    clearDisplay();
    delay(200);
  }
}

void animateSmiley() {
  for (int i = 0; i < 5; i++) {
    displayPattern(smiley);
    delay(300);
    clearDisplay();
    delay(100);
  }
}

// Drawing functions for LED matrix
void drawPixel(int x, int y) {
  if (x >= 0 && x < 16 && y >= 0 && y < 16) {
    int ledIndex = y * 16 + x;
    if (ledIndex < NUM_LEDS) {
      leds[ledIndex] = CRGB::White;
    }
  }
}

void clearPixel(int x, int y) {
  if (x >= 0 && x < 16 && y >= 0 && y < 16) {
    int ledIndex = y * 16 + x;
    if (ledIndex < NUM_LEDS) {
      leds[ledIndex] = CRGB::Black;
    }
  }
}

void drawLine(int x1, int y1, int x2, int y2) {
  int dx = abs(x2 - x1);
  int dy = abs(y2 - y1);
  int sx = x1 < x2 ? 1 : -1;
  int sy = y1 < y2 ? 1 : -1;
  int err = dx - dy;
  
  while (true) {
    drawPixel(x1, y1);
    if (x1 == x2 && y1 == y2) break;
    int e2 = 2 * err;
    if (e2 > -dy) {
      err -= dy;
      x1 += sx;
    }
    if (e2 < dx) {
      err += dx;
      y1 += sy;
    }
  }
  FastLED.show();
}

void drawCircle(int centerX, int centerY, int radius) {
  for (int x = -radius; x <= radius; x++) {
    for (int y = -radius; y <= radius; y++) {
      if (x * x + y * y <= radius * radius) {
        drawPixel(centerX + x, centerY + y);
      }
    }
  }
  FastLED.show();
}
