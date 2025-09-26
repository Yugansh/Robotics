"""
Basic Movement Examples for Cardboard Robot (No Hardware Required)
Demonstrates fundamental movement commands using mock controller
"""

import sys
import os

# Add the python directory to the path
current_dir = os.path.dirname(os.path.abspath(__file__))
python_dir = os.path.join(current_dir, '..', 'python')
sys.path.insert(0, python_dir)

from robot_controller_mock import CardboardRobot
import time

def basic_movement_demo():
    """Demonstrate basic movement commands"""
    print("=== Basic Movement Demo (Mock) ===")
    
    robot = CardboardRobot()
    
    if not robot.connect():
        print("Could not connect to robot. Please check connections.")
        return
    
    try:
        print("Testing basic movements...")
        
        # Forward movement
        print("Moving forward for 2 seconds...")
        robot.move_forward(2.0)
        time.sleep(1)
        
        # Backward movement
        print("Moving backward for 2 seconds...")
        robot.move_backward(2.0)
        time.sleep(1)
        
        # Left turn
        print("Turning left for 1 second...")
        robot.turn_left(1.0)
        time.sleep(1)
        
        # Right turn
        print("Turning right for 1 second...")
        robot.turn_right(1.0)
        time.sleep(1)
        
        # Stop
        print("Stopping...")
        robot.stop()
        
        print("Basic movement demo complete!")
        
    except KeyboardInterrupt:
        print("\nDemo interrupted by user")
    finally:
        robot.disconnect()

def speed_test():
    """Test different movement speeds"""
    print("=== Speed Test (Mock) ===")
    
    robot = CardboardRobot()
    
    if not robot.connect():
        print("Could not connect to robot. Please check connections.")
        return
    
    try:
        speeds = ['slow', 'normal', 'fast']
        
        for speed in speeds:
            print(f"Testing {speed} speed...")
            robot.set_speed(speed)
            robot.move_forward(1.0)
            time.sleep(0.5)
        
        print("Speed test complete!")
        
    except KeyboardInterrupt:
        print("\nTest interrupted by user")
    finally:
        robot.disconnect()

def square_dance():
    """Make the robot dance in a square pattern"""
    print("=== Square Dance (Mock) ===")
    
    robot = CardboardRobot()
    
    if not robot.connect():
        print("Could not connect to robot. Please check connections.")
        return
    
    try:
        print("Starting square dance...")
        
        # Dance in a square
        for i in range(4):
            print(f"Square dance step {i+1}/4")
            
            # Move forward
            robot.move_forward(1.5)
            time.sleep(0.5)
            
            # Turn right
            robot.turn_right(0.8)
            time.sleep(0.5)
        
        print("Square dance complete!")
        
    except KeyboardInterrupt:
        print("\nDance interrupted by user")
    finally:
        robot.disconnect()

def obstacle_course():
    """Navigate a simple obstacle course"""
    print("=== Obstacle Course (Mock) ===")
    
    robot = CardboardRobot()
    
    if not robot.connect():
        print("Could not connect to robot. Please check connections.")
        return
    
    try:
        print("Starting obstacle course...")
        
        # Course sequence
        moves = [
            ("forward", 2.0, "Moving forward"),
            ("right", 1.0, "Turning right"),
            ("forward", 1.5, "Moving forward"),
            ("left", 1.0, "Turning left"),
            ("forward", 2.0, "Moving forward"),
            ("right", 1.0, "Turning right"),
            ("backward", 1.0, "Moving backward"),
            ("left", 1.0, "Turning left"),
            ("forward", 1.0, "Final forward")
        ]
        
        for move, duration, description in moves:
            print(description)
            
            if move == "forward":
                robot.move_forward(duration)
            elif move == "backward":
                robot.move_backward(duration)
            elif move == "left":
                robot.turn_left(duration)
            elif move == "right":
                robot.turn_right(duration)
            
            time.sleep(0.5)
        
        print("Obstacle course complete!")
        
    except KeyboardInterrupt:
        print("\nCourse interrupted by user")
    finally:
        robot.disconnect()

def main():
    """Main function to run movement examples"""
    print("Cardboard Robot Movement Examples (Mock - No Hardware Required)")
    print("==============================================================")
    
    while True:
        print("\nChoose an example:")
        print("1. Basic Movement Demo")
        print("2. Speed Test")
        print("3. Square Dance")
        print("4. Obstacle Course")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            basic_movement_demo()
        elif choice == '2':
            speed_test()
        elif choice == '3':
            square_dance()
        elif choice == '4':
            obstacle_course()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
