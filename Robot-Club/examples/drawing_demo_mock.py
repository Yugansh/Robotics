"""
Drawing Demo for Cardboard Robot (No Hardware Required)
Combines movement and LED matrix drawing for artistic demonstrations using mock controller
"""

import sys
import os

# Add the python directory to the path
current_dir = os.path.dirname(os.path.abspath(__file__))
python_dir = os.path.join(current_dir, '..', 'python')
sys.path.insert(0, python_dir)

from robot_controller_mock import CardboardRobot
from pattern_generator import LEDPatternGenerator
import time

def drawing_with_movement():
    """Combine drawing patterns with robot movement"""
    print("=== Drawing with Movement Demo (Mock) ===")
    
    robot = CardboardRobot()
    
    if not robot.connect():
        print("Could not connect to robot. Please check connections.")
        return
    
    try:
        print("Starting drawing with movement demo...")
        
        # Sequence of movements with different patterns
        drawing_sequence = [
            ("forward", 1.0, "heart", "Drawing a heart while moving forward"),
            ("right", 0.8, "arrow", "Showing arrow while turning right"),
            ("forward", 1.5, "pattern", "Drawing a pattern while moving forward"),
            ("left", 0.8, "arrow", "Showing arrow while turning left"),
            ("backward", 1.0, "heart", "Drawing heart while moving backward"),
            ("stop", 0, "pattern", "Final pattern")
        ]
        
        for movement, duration, pattern, description in drawing_sequence:
            print(description)
            
            # Display pattern
            robot.display_pattern(pattern)
            
            # Perform movement
            if movement == "forward":
                robot.move_forward(duration)
            elif movement == "backward":
                robot.move_backward(duration)
            elif movement == "left":
                robot.turn_left(duration)
            elif movement == "right":
                robot.turn_right(duration)
            elif movement == "stop":
                robot.stop()
            
            time.sleep(0.5)
        
        print("Drawing with movement demo complete!")
        
    except KeyboardInterrupt:
        print("\nDemo interrupted by user")
    finally:
        robot.disconnect()

def pattern_showcase():
    """Showcase different patterns in sequence"""
    print("=== Pattern Showcase (Mock) ===")
    
    robot = CardboardRobot()
    
    if not robot.connect():
        print("Could not connect to robot. Please check connections.")
        return
    
    try:
        print("Starting pattern showcase...")
        
        # Showcase patterns
        showcase_patterns = [
            ("heart", 2.0, "Love pattern"),
            ("arrow", 1.5, "Direction indicator"),
            ("pattern", 2.0, "Default pattern"),
            ("clear", 0.5, "Clear display")
        ]
        
        for pattern, duration, description in showcase_patterns:
            print(f"Displaying: {description}")
            robot.display_pattern(pattern)
            time.sleep(duration)
        
        print("Pattern showcase complete!")
        
    except KeyboardInterrupt:
        print("\nShowcase interrupted by user")
    finally:
        robot.disconnect()

def artistic_dance():
    """Perform an artistic dance with patterns"""
    print("=== Artistic Dance (Mock) ===")
    
    robot = CardboardRobot()
    
    if not robot.connect():
        print("Could not connect to robot. Please check connections.")
        return
    
    try:
        print("Starting artistic dance...")
        
        # Dance moves with patterns
        dance_moves = [
            ("forward", 0.5, "heart", "Love forward"),
            ("right", 0.4, "arrow", "Turn with arrow"),
            ("forward", 0.5, "pattern", "Pattern forward"),
            ("left", 0.4, "arrow", "Arrow turn"),
            ("backward", 0.5, "heart", "Happy backward"),
            ("right", 0.4, "arrow", "Arrow turn"),
            ("forward", 0.5, "pattern", "Pattern forward"),
            ("left", 0.4, "arrow", "Arrow turn"),
            ("stop", 0, "pattern", "Final pose")
        ]
        
        for movement, duration, pattern, description in dance_moves:
            print(description)
            
            # Display pattern
            robot.display_pattern(pattern)
            
            # Perform movement
            if movement == "forward":
                robot.move_forward(duration)
            elif movement == "backward":
                robot.move_backward(duration)
            elif movement == "left":
                robot.turn_left(duration)
            elif movement == "right":
                robot.turn_right(duration)
            elif movement == "stop":
                robot.stop()
            
            time.sleep(0.3)
        
        print("Artistic dance complete!")
        
    except KeyboardInterrupt:
        print("\nDance interrupted by user")
    finally:
        robot.disconnect()

def pattern_animation():
    """Animate patterns on the LED matrix"""
    print("=== Pattern Animation (Mock) ===")
    
    robot = CardboardRobot()
    
    if not robot.connect():
        print("Could not connect to robot. Please check connections.")
        return
    
    try:
        print("Starting pattern animation...")
        
        # Create animation sequences
        animations = [
            ("heart", 3, "Heart animation"),
            ("arrow", 4, "Arrow rotation"),
            ("pattern", 5, "Pattern animation")
        ]
        
        for pattern_name, frames, description in animations:
            print(description)
            
            # Create animation frames
            generator = LEDPatternGenerator()
            animation_frames = generator.create_animation_frames(pattern_name, frames)
            
            # Display each frame
            for i, frame in enumerate(animation_frames):
                print(f"Frame {i+1}/{frames}")
                # Convert frame to custom pattern and display
                robot.draw_custom_pattern(frame)
                time.sleep(0.5)
            
            time.sleep(1)
        
        print("Pattern animation complete!")
        
    except KeyboardInterrupt:
        print("\nAnimation interrupted by user")
    finally:
        robot.disconnect()

def interactive_drawing():
    """Interactive drawing session"""
    print("=== Interactive Drawing (Mock) ===")
    
    robot = CardboardRobot()
    
    if not robot.connect():
        print("Could not connect to robot. Please check connections.")
        return
    
    try:
        print("Interactive drawing session started!")
        print("Commands: f(forward), b(backward), l(left), r(right), s(stop)")
        print("Patterns: h(heart), a(arrow), p(pattern), c(clear)")
        print("Special: d(dance), show(showcase), q(quit)")
        
        while True:
            command = input("Enter command: ").lower().strip()
            
            if command == 'q':
                break
            elif command == 'f':
                robot.move_forward()
            elif command == 'b':
                robot.move_backward()
            elif command == 'l':
                robot.turn_left()
            elif command == 'r':
                robot.turn_right()
            elif command == 's':
                robot.stop()
            elif command == 'h':
                robot.display_pattern('heart')
            elif command == 'a':
                robot.display_pattern('arrow')
            elif command == 'p':
                robot.display_pattern('pattern')
            elif command == 'c':
                robot.clear_display()
            elif command == 'd':
                artistic_dance()
            elif command == 'show':
                pattern_showcase()
            else:
                print("Unknown command. Type 'q' to quit.")
        
        print("Interactive drawing session ended")
        
    except KeyboardInterrupt:
        print("\nSession interrupted by user")
    finally:
        robot.disconnect()

def main():
    """Main function to run drawing demos"""
    print("Cardboard Robot Drawing Demo (Mock - No Hardware Required)")
    print("=========================================================")
    
    while True:
        print("\nChoose a demo:")
        print("1. Drawing with Movement")
        print("2. Pattern Showcase")
        print("3. Artistic Dance")
        print("4. Pattern Animation")
        print("5. Interactive Drawing")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            drawing_with_movement()
        elif choice == '2':
            pattern_showcase()
        elif choice == '3':
            artistic_dance()
        elif choice == '4':
            pattern_animation()
        elif choice == '5':
            interactive_drawing()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
