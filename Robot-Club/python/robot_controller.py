"""
Cardboard Robot Controller
Python interface for controlling the cardboard robot with LED matrix drawing
"""

import serial
import time
import numpy as np
from typing import List, Tuple, Optional

class CardboardRobot:
    def __init__(self, port: str = None, baudrate: int = 9600):
        """
        Initialize the cardboard robot controller
        
        Args:
            port: Serial port (e.g., 'COM3' on Windows, '/dev/ttyUSB0' on Linux)
            baudrate: Serial communication baud rate
        """
        self.port = port
        self.baudrate = baudrate
        self.serial_connection = None
        self.is_connected = False
        
        # Movement constants
        self.MOVEMENT_COMMANDS = {
            'forward': 'F',
            'backward': 'B',
            'left': 'L',
            'right': 'R',
            'stop': 'S'
        }
        
        # LED commands
        self.LED_COMMANDS = {
            'pattern': 'P',
            'clear': 'C',
            'heart': 'H',
            'arrow': 'A'
        }
        
        # Speed settings
        self.SPEED_COMMANDS = {
            'slow': '1',
            'normal': '2',
            'fast': '3'
        }
    
    def connect(self, port: str = None) -> bool:
        """
        Connect to the robot via serial communication
        
        Args:
            port: Serial port to connect to
            
        Returns:
            True if connection successful, False otherwise
        """
        if port:
            self.port = port
            
        if not self.port:
            # Try to auto-detect port
            self.port = self._auto_detect_port()
            
        if not self.port:
            print("Error: No serial port specified or detected")
            return False
            
        try:
            self.serial_connection = serial.Serial(
                self.port, 
                self.baudrate, 
                timeout=1
            )
            time.sleep(2)  # Wait for Arduino to initialize
            self.is_connected = True
            print(f"Connected to robot on {self.port}")
            return True
        except serial.SerialException as e:
            print(f"Failed to connect to robot: {e}")
            return False
    
    def disconnect(self):
        """Disconnect from the robot"""
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            self.is_connected = False
            print("Disconnected from robot")
    
    def _auto_detect_port(self) -> Optional[str]:
        """Auto-detect Arduino port"""
        import serial.tools.list_ports
        
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if 'Arduino' in port.description or 'USB' in port.description:
                return port.device
        return None
    
    def _send_command(self, command: str) -> bool:
        """
        Send command to the robot
        
        Args:
            command: Command string to send
            
        Returns:
            True if command sent successfully, False otherwise
        """
        if not self.is_connected or not self.serial_connection:
            print("Error: Robot not connected")
            return False
            
        try:
            self.serial_connection.write(command.encode())
            time.sleep(0.1)  # Small delay for command processing
            return True
        except Exception as e:
            print(f"Error sending command: {e}")
            return False
    
    def move_forward(self, duration: float = 1.0):
        """Move robot forward"""
        print("Moving forward...")
        self._send_command(self.MOVEMENT_COMMANDS['forward'])
        time.sleep(duration)
        self.stop()
    
    def move_backward(self, duration: float = 1.0):
        """Move robot backward"""
        print("Moving backward...")
        self._send_command(self.MOVEMENT_COMMANDS['backward'])
        time.sleep(duration)
        self.stop()
    
    def turn_left(self, duration: float = 1.0):
        """Turn robot left"""
        print("Turning left...")
        self._send_command(self.MOVEMENT_COMMANDS['left'])
        time.sleep(duration)
        self.stop()
    
    def turn_right(self, duration: float = 1.0):
        """Turn robot right"""
        print("Turning right...")
        self._send_command(self.MOVEMENT_COMMANDS['right'])
        time.sleep(duration)
        self.stop()
    
    def stop(self):
        """Stop robot movement"""
        print("Stopping...")
        self._send_command(self.MOVEMENT_COMMANDS['stop'])
    
    def set_speed(self, speed: str):
        """Set movement speed"""
        if speed in self.SPEED_COMMANDS:
            print(f"Setting speed to {speed}")
            self._send_command(self.SPEED_COMMANDS[speed])
        else:
            print(f"Invalid speed: {speed}. Use 'slow', 'normal', or 'fast'")
    
    def display_pattern(self, pattern: str = 'pattern'):
        """Display a pattern on the LED matrix"""
        if pattern in self.LED_COMMANDS:
            print(f"Displaying {pattern} pattern")
            self._send_command(self.LED_COMMANDS[pattern])
        else:
            print(f"Invalid pattern: {pattern}")
    
    def clear_display(self):
        """Clear the LED matrix display"""
        print("Clearing display")
        self._send_command(self.LED_COMMANDS['clear'])
    
    def draw_custom_pattern(self, pattern: List[List[int]]):
        """
        Draw a custom 8x8 pattern on the LED matrix
        
        Args:
            pattern: 8x8 matrix of 0s and 1s representing the pattern
        """
        if len(pattern) != 8 or any(len(row) != 8 for row in pattern):
            print("Error: Pattern must be 8x8")
            return
            
        print("Drawing custom pattern...")
        # Convert pattern to binary string and send
        # This would require additional Arduino code to handle custom patterns
        # For now, we'll use the predefined patterns
        self.display_pattern('pattern')
    
    def dance_sequence(self):
        """Perform a dance sequence"""
        print("Starting dance sequence...")
        
        # Dance moves
        moves = [
            ('forward', 0.5),
            ('turn_left', 0.3),
            ('turn_right', 0.3),
            ('backward', 0.5),
            ('turn_right', 0.3),
            ('turn_left', 0.3),
        ]
        
        for move, duration in moves:
            if move == 'forward':
                self.move_forward(duration)
            elif move == 'backward':
                self.move_backward(duration)
            elif move == 'turn_left':
                self.turn_left(duration)
            elif move == 'turn_right':
                self.turn_right(duration)
            
            # Display different patterns during dance
            if move == 'forward':
                self.display_pattern('arrow')
            elif move == 'backward':
                self.display_pattern('arrow')
            else:
                self.display_pattern('heart')
            
            time.sleep(0.2)
        
        self.display_pattern('smiley')
        print("Dance sequence complete!")
    
    def drawing_demo(self):
        """Demonstrate LED matrix drawing capabilities"""
        print("Starting drawing demo...")
        
        patterns = ['heart', 'arrow', 'pattern', 'clear']
        
        for pattern in patterns:
            print(f"Displaying {pattern}")
            self.display_pattern(pattern)
            time.sleep(2)
        
        print("Drawing demo complete!")
    
    def interactive_mode(self):
        """Start interactive control mode"""
        print("Interactive mode started!")
        print("Commands: f(forward), b(backward), l(left), r(right), s(stop)")
        print("LED: h(heart), a(arrow), p(pattern), c(clear)")
        print("Speed: 1(slow), 2(normal), 3(fast)")
        print("Special: d(dance), demo(drawing demo), q(quit)")
        
        while True:
            try:
                command = input("Enter command: ").lower().strip()
                
                if command == 'q':
                    break
                elif command == 'f':
                    self.move_forward()
                elif command == 'b':
                    self.move_backward()
                elif command == 'l':
                    self.turn_left()
                elif command == 'r':
                    self.turn_right()
                elif command == 's':
                    self.stop()
                elif command == 'h':
                    self.display_pattern('heart')
                elif command == 'a':
                    self.display_pattern('arrow')
                elif command == 'p':
                    self.display_pattern('pattern')
                elif command == 'c':
                    self.clear_display()
                elif command == '1':
                    self.set_speed('slow')
                elif command == '2':
                    self.set_speed('normal')
                elif command == '3':
                    self.set_speed('fast')
                elif command == 'd':
                    self.dance_sequence()
                elif command == 'demo':
                    self.drawing_demo()
                else:
                    print("Unknown command. Type 'q' to quit.")
                    
            except KeyboardInterrupt:
                break
        
        print("Interactive mode ended")
        self.stop()
        self.clear_display()

def main():
    """Main function for testing the robot controller"""
    robot = CardboardRobot()
    
    # Try to connect
    if robot.connect():
        try:
            # Run interactive mode
            robot.interactive_mode()
        finally:
            robot.disconnect()
    else:
        print("Could not connect to robot. Please check connections and try again.")

if __name__ == "__main__":
    main()
