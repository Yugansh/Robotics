"""
LED Pattern Demo for Cardboard Robot (No Hardware Required)
Demonstrates LED matrix drawing and pattern generation without robot hardware
"""

import sys
import os

# Add the python directory to the path
current_dir = os.path.dirname(os.path.abspath(__file__))
python_dir = os.path.join(current_dir, '..', 'python')
sys.path.insert(0, python_dir)

from pattern_generator import LEDPatternGenerator
import time

def pattern_generator_demo():
    """Demonstrate pattern generation capabilities"""
    print("=== Pattern Generator Demo ===")
    
    generator = LEDPatternGenerator()
    
    print("Available patterns:", generator.list_patterns())
    
    # Display some patterns
    patterns_to_show = ['smiley', 'heart', 'star', 'diamond', 'spiral']
    
    for pattern_name in patterns_to_show:
        print(f"\n{pattern_name.upper()} pattern:")
        pattern = generator.get_pattern(pattern_name)
        if pattern:
            for row in pattern:
                print(' '.join('█' if bit else ' ' for bit in row))
            
            # Convert to Arduino format
            arduino_bytes = generator.convert_to_arduino_bytes(pattern)
            print(f"Arduino bytes: {arduino_bytes}")

def custom_pattern_demo():
    """Create and display custom patterns"""
    print("=== Custom Pattern Demo ===")
    
    generator = LEDPatternGenerator()
    
    # Create a custom diagonal pattern
    print("Creating diagonal pattern...")
    diagonal_points = [(i, i) for i in range(8)]
    diagonal_pattern = generator.create_custom_pattern(diagonal_points)
    
    print("Diagonal pattern:")
    for row in diagonal_pattern:
        print(' '.join('█' if bit else ' ' for bit in row))
    
    # Create a custom border pattern
    print("\nCreating border pattern...")
    border_points = []
    for i in range(8):
        border_points.extend([(0, i), (7, i), (i, 0), (i, 7)])
    border_pattern = generator.create_custom_pattern(border_points)
    
    print("Border pattern:")
    for row in border_pattern:
        print(' '.join('█' if bit else ' ' for bit in row))
    
    # Create a custom cross pattern
    print("\nCreating cross pattern...")
    cross_points = [(3, i) for i in range(8)] + [(i, 3) for i in range(8)]
    cross_pattern = generator.create_custom_pattern(cross_points)
    
    print("Cross pattern:")
    for row in cross_pattern:
        print(' '.join('█' if bit else ' ' for bit in row))

def drawing_demo():
    """Demonstrate drawing functions"""
    print("=== Drawing Demo ===")
    
    generator = LEDPatternGenerator()
    
    # Draw a line
    print("Drawing a line from (0,0) to (7,7)...")
    line_pattern = generator.draw_line(0, 0, 7, 7)
    print("Line pattern:")
    for row in line_pattern:
        print(' '.join('█' if bit else ' ' for bit in row))
    
    # Draw a circle
    print("\nDrawing a circle at center (3,3) with radius 2...")
    circle_pattern = generator.draw_circle(3, 3, 2)
    print("Circle pattern:")
    for row in circle_pattern:
        print(' '.join('█' if bit else ' ' for bit in row))
    
    # Draw a heart using points
    print("\nDrawing a heart using point coordinates...")
    heart_points = [
        (1, 2), (2, 1), (3, 1), (4, 1), (5, 2), (6, 2),
        (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),
        (2, 4), (3, 4), (4, 4), (5, 4),
        (3, 5), (4, 5),
        (3, 6)
    ]
    custom_heart = generator.create_custom_pattern(heart_points)
    print("Custom heart pattern:")
    for row in custom_heart:
        print(' '.join('█' if bit else ' ' for bit in row))

def animation_demo():
    """Demonstrate animation capabilities"""
    print("=== Animation Demo ===")
    
    generator = LEDPatternGenerator()
    
    # Create rotating star animation
    print("Creating rotating star animation...")
    star_frames = generator.create_animation_frames('star', 8)
    
    print("Star animation frames:")
    for i, frame in enumerate(star_frames):
        print(f"Frame {i+1}:")
        for row in frame:
            print(' '.join('█' if bit else ' ' for bit in row))
        print()

def interactive_pattern_creator():
    """Interactive pattern creation tool"""
    print("=== Interactive Pattern Creator ===")
    
    generator = LEDPatternGenerator()
    
    while True:
        print("\nPattern Creator Menu:")
        print("1. View predefined patterns")
        print("2. Create custom pattern")
        print("3. Draw a line")
        print("4. Draw a circle")
        print("5. Create animation")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            print("\nPredefined patterns:")
            for i, pattern_name in enumerate(generator.list_patterns(), 1):
                print(f"{i}. {pattern_name}")
            
            try:
                pattern_choice = int(input("Enter pattern number: ")) - 1
                pattern_names = generator.list_patterns()
                if 0 <= pattern_choice < len(pattern_names):
                    pattern_name = pattern_names[pattern_choice]
                    pattern = generator.get_pattern(pattern_name)
                    print(f"\n{pattern_name.upper()} pattern:")
                    for row in pattern:
                        print(' '.join('█' if bit else ' ' for bit in row))
                else:
                    print("Invalid pattern number")
            except ValueError:
                print("Invalid input")
        
        elif choice == '2':
            print("\nEnter coordinates (x,y) to turn on pixels.")
            print("Enter 'done' when finished.")
            points = []
            while True:
                coord_input = input("Enter coordinate (x,y) or 'done': ").strip()
                if coord_input.lower() == 'done':
                    break
                try:
                    x, y = map(int, coord_input.split(','))
                    if 0 <= x < 8 and 0 <= y < 8:
                        points.append((x, y))
                        print(f"Added point ({x}, {y})")
                    else:
                        print("Coordinates must be between 0 and 7")
                except ValueError:
                    print("Invalid format. Use 'x,y' format")
            
            if points:
                pattern = generator.create_custom_pattern(points)
                print("\nCustom pattern:")
                for row in pattern:
                    print(' '.join('█' if bit else ' ' for bit in row))
        
        elif choice == '3':
            try:
                x1 = int(input("Enter start x: "))
                y1 = int(input("Enter start y: "))
                x2 = int(input("Enter end x: "))
                y2 = int(input("Enter end y: "))
                
                if all(0 <= coord < 8 for coord in [x1, y1, x2, y2]):
                    pattern = generator.draw_line(x1, y1, x2, y2)
                    print("\nLine pattern:")
                    for row in pattern:
                        print(' '.join('█' if bit else ' ' for bit in row))
                else:
                    print("Coordinates must be between 0 and 7")
            except ValueError:
                print("Invalid input")
        
        elif choice == '4':
            try:
                center_x = int(input("Enter center x: "))
                center_y = int(input("Enter center y: "))
                radius = int(input("Enter radius: "))
                
                if all(0 <= coord < 8 for coord in [center_x, center_y]) and 0 < radius < 8:
                    pattern = generator.draw_circle(center_x, center_y, radius)
                    print("\nCircle pattern:")
                    for row in pattern:
                        print(' '.join('█' if bit else ' ' for bit in row))
                else:
                    print("Invalid parameters")
            except ValueError:
                print("Invalid input")
        
        elif choice == '5':
            print("\nAvailable patterns for animation:")
            for i, pattern_name in enumerate(generator.list_patterns(), 1):
                print(f"{i}. {pattern_name}")
            
            try:
                pattern_choice = int(input("Enter pattern number: ")) - 1
                frames = int(input("Enter number of frames: "))
                
                pattern_names = generator.list_patterns()
                if 0 <= pattern_choice < len(pattern_names):
                    pattern_name = pattern_names[pattern_choice]
                    animation = generator.create_animation_frames(pattern_name, frames)
                    print(f"\n{pattern_name} animation ({frames} frames):")
                    for i, frame in enumerate(animation):
                        print(f"Frame {i+1}:")
                        for row in frame:
                            print(' '.join('█' if bit else ' ' for bit in row))
                        print()
                else:
                    print("Invalid pattern number")
            except ValueError:
                print("Invalid input")
        
        elif choice == '6':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

def main():
    """Main function to run LED pattern examples"""
    print("Cardboard Robot LED Pattern Demo (No Hardware Required)")
    print("=======================================================")
    
    while True:
        print("\nChoose an example:")
        print("1. Pattern Generator Demo")
        print("2. Custom Pattern Demo")
        print("3. Drawing Demo")
        print("4. Animation Demo")
        print("5. Interactive Pattern Creator")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            pattern_generator_demo()
        elif choice == '2':
            custom_pattern_demo()
        elif choice == '3':
            drawing_demo()
        elif choice == '4':
            animation_demo()
        elif choice == '5':
            interactive_pattern_creator()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
