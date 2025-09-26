"""
Mock Cardboard Robot Controller (No Hardware Required)
Python interface for testing the cardboard robot without hardware dependencies
"""

import time
from typing import List, Tuple, Optional

class CardboardRobot:
    def __init__(self, port: str = None, baudrate: int = 9600):
        """
        Initialize the cardboard robot controller (mock version)
        
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
        Connect to the robot via serial communication (mock)
        
        Args:
            port: Serial port to connect to
            
        Returns:
            True if connection successful, False otherwise
        """
        if port:
            self.port = port
            
        # Mock connection - always succeeds
        self.is_connected = True
        print(f"Mock connected to robot on {self.port or 'mock_port'}")
        return True
    
    def disconnect(self):
        """Disconnect from the robot"""
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
        self.is_connected = False
        print("Mock disconnected from robot")
    
    def _send_command(self, command: str) -> bool:
        """
        Send command to the robot (mock)
        
        Args:
            command: Command string to send
            
        Returns:
            True if command sent successfully, False otherwise
        """
        if not self.is_connected:
            print("Error: Robot not connected")
            return False
            
        print(f"Mock sending command: {command}")
        time.sleep(0.1)  # Simulate command processing
        return True
    
    def move_forward(self, duration: float = 1.0):
        """Move robot forward (mock)"""
        print("Mock moving forward...")
        self._send_command(self.MOVEMENT_COMMANDS['forward'])
        time.sleep(duration)
        self.stop()
    
    def move_backward(self, duration: float = 1.0):
        """Move robot backward (mock)"""
        print("Mock moving backward...")
        self._send_command(self.MOVEMENT_COMMANDS['backward'])
        time.sleep(duration)
        self.stop()
    
    def turn_left(self, duration: float = 1.0):
        """Turn robot left (mock)"""
        print("Mock turning left...")
        self._send_command(self.MOVEMENT_COMMANDS['left'])
        time.sleep(duration)
        self.stop()
    
    def turn_right(self, duration: float = 1.0):
        """Turn robot right (mock)"""
        print("Mock turning right...")
        self._send_command(self.MOVEMENT_COMMANDS['right'])
        time.sleep(duration)
        self.stop()
    
    def stop(self):
        """Stop robot movement (mock)"""
        print("Mock stopping...")
        self._send_command(self.MOVEMENT_COMMANDS['stop'])
    
    def set_speed(self, speed: str):
        """Set movement speed (mock)"""
        if speed in self.SPEED_COMMANDS:
            print(f"Mock setting speed to {speed}")
            self._send_command(self.SPEED_COMMANDS[speed])
        else:
            print(f"Invalid speed: {speed}. Use 'slow', 'normal', or 'fast'")
    
    def display_pattern(self, pattern: str = 'pattern'):
        """Display a pattern on the LED matrix (mock)"""
        if pattern in self.LED_COMMANDS:
            print(f"Mock displaying {pattern} pattern")
            self._send_command(self.LED_COMMANDS[pattern])
        else:
            print(f"Invalid pattern: {pattern}")
    
    def clear_display(self):
        """Clear the LED matrix display (mock)"""
        print("Mock clearing display")
        self._send_command(self.LED_COMMANDS['clear'])
    
    def draw_custom_pattern(self, pattern: List[List[int]]):
        """
        Draw a custom 8x8 pattern on the LED matrix (mock)
        
        Args:
            pattern: 8x8 matrix of 0s and 1s representing the pattern
        """
        if len(pattern) != 8 or any(len(row) != 8 for row in pattern):
            print("Error: Pattern must be 8x8")
            return
            
        print("Mock drawing custom pattern...")
        # Display the pattern
        for row in pattern:
            print(' '.join('█' if bit else ' ' for bit in row))
    
    def dance_sequence(self):
        """Perform a dance sequence (mock)"""
        print("Mock starting dance sequence...")
        
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
        
        self.display_pattern('pattern')
        print("Mock dance sequence complete!")
    
    def drawing_demo(self):
        """Demonstrate LED matrix drawing capabilities (mock)"""
        print("Mock starting drawing demo...")
        
        patterns = ['heart', 'arrow', 'pattern', 'clear']
        
        for pattern in patterns:
            print(f"Mock displaying {pattern}")
            self.display_pattern(pattern)
            time.sleep(2)
        
        print("Mock drawing demo complete!")
    
    def interactive_mode(self):
        """Start interactive control mode (mock)"""
        print("Mock interactive mode started!")
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
        
        print("Mock interactive mode ended")
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
