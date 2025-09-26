"""
LED Pattern Generator for Cardboard Robot
Generates and converts patterns for the 8x8 LED matrix
"""

import numpy as np
from typing import List, Tuple, Optional
import matplotlib.pyplot as plt
from PIL import Image

class LEDPatternGenerator:
    def __init__(self):
        """Initialize the pattern generator"""
        self.matrix_size = 8
        
        # Predefined patterns
        self.patterns = {
            'smiley': self._create_smiley(),
            'heart': self._create_heart(),
            'arrow': self._create_arrow(),
            'robot': self._create_robot(),
            'star': self._create_star(),
            'diamond': self._create_diamond(),
            'checker': self._create_checker(),
            'spiral': self._create_spiral(),
            'wave': self._create_wave(),
            'cross': self._create_cross()
        }
    
    def _create_smiley(self) -> List[List[int]]:
        """Create a smiley face pattern"""
        return [
            [0, 0, 1, 1, 1, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 0],
            [1, 0, 1, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 1, 0, 1],
            [1, 0, 0, 1, 1, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 1, 1, 1, 0, 0]
        ]
    
    def _create_heart(self) -> List[List[int]]:
        """Create a heart pattern"""
        return [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
    
    def _create_arrow(self) -> List[List[int]]:
        """Create an arrow pattern"""
        return [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
    
    def _create_robot(self) -> List[List[int]]:
        """Create a robot face pattern"""
        return [
            [0, 0, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 0, 0, 0, 0, 1, 1],
            [1, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 1],
            [1, 1, 0, 0, 0, 0, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 0, 0]
        ]
    
    def _create_star(self) -> List[List[int]]:
        """Create a star pattern"""
        return [
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0]
        ]
    
    def _create_diamond(self) -> List[List[int]]:
        """Create a diamond pattern"""
        return [
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0]
        ]
    
    def _create_checker(self) -> List[List[int]]:
        """Create a checkerboard pattern"""
        return [
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1]
        ]
    
    def _create_spiral(self) -> List[List[int]]:
        """Create a spiral pattern"""
        return [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 1]
        ]
    
    def _create_wave(self) -> List[List[int]]:
        """Create a wave pattern"""
        return [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 0],
            [1, 0, 1, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
    
    def _create_cross(self) -> List[List[int]]:
        """Create a cross pattern"""
        return [
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0]
        ]
    
    def get_pattern(self, name: str) -> Optional[List[List[int]]]:
        """Get a predefined pattern by name"""
        return self.patterns.get(name)
    
    def list_patterns(self) -> List[str]:
        """Get list of available pattern names"""
        return list(self.patterns.keys())
    
    def create_custom_pattern(self, points: List[Tuple[int, int]]) -> List[List[int]]:
        """
        Create a custom pattern from a list of points
        
        Args:
            points: List of (x, y) coordinates to turn on
            
        Returns:
            8x8 pattern matrix
        """
        pattern = [[0 for _ in range(8)] for _ in range(8)]
        
        for x, y in points:
            if 0 <= x < 8 and 0 <= y < 8:
                pattern[y][x] = 1
        
        return pattern
    
    def draw_line(self, x1: int, y1: int, x2: int, y2: int) -> List[List[int]]:
        """
        Draw a line between two points using Bresenham's algorithm
        
        Args:
            x1, y1: Start point
            x2, y2: End point
            
        Returns:
            8x8 pattern matrix with line drawn
        """
        pattern = [[0 for _ in range(8)] for _ in range(8)]
        
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy
        
        while True:
            if 0 <= x1 < 8 and 0 <= y1 < 8:
                pattern[y1][x1] = 1
            
            if x1 == x2 and y1 == y2:
                break
                
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy
        
        return pattern
    
    def draw_circle(self, center_x: int, center_y: int, radius: int) -> List[List[int]]:
        """
        Draw a circle
        
        Args:
            center_x, center_y: Circle center
            radius: Circle radius
            
        Returns:
            8x8 pattern matrix with circle drawn
        """
        pattern = [[0 for _ in range(8)] for _ in range(8)]
        
        for x in range(8):
            for y in range(8):
                if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2:
                    pattern[y][x] = 1
        
        return pattern
    
    def convert_to_arduino_bytes(self, pattern: List[List[int]]) -> List[int]:
        """
        Convert pattern to Arduino byte format
        
        Args:
            pattern: 8x8 pattern matrix
            
        Returns:
            List of 8 bytes for Arduino
        """
        bytes_list = []
        for row in pattern:
            byte_val = 0
            for i, bit in enumerate(row):
                if bit:
                    byte_val |= (1 << (7 - i))
            bytes_list.append(byte_val)
        return bytes_list
    
    def display_pattern(self, pattern: List[List[int]], title: str = "LED Pattern"):
        """
        Display pattern using matplotlib
        
        Args:
            pattern: 8x8 pattern matrix
            title: Title for the plot
        """
        plt.figure(figsize=(6, 6))
        plt.imshow(pattern, cmap='binary', interpolation='nearest')
        plt.title(title)
        plt.xticks(range(8))
        plt.yticks(range(8))
        plt.grid(True, alpha=0.3)
        plt.show()
    
    def save_pattern(self, pattern: List[List[int]], filename: str):
        """
        Save pattern as an image
        
        Args:
            pattern: 8x8 pattern matrix
            filename: Output filename
        """
        # Convert to numpy array and scale up
        pattern_array = np.array(pattern) * 255
        pattern_image = Image.fromarray(pattern_array.astype(np.uint8))
        
        # Scale up for better visibility
        scaled_image = pattern_image.resize((80, 80), Image.NEAREST)
        scaled_image.save(filename)
    
    def create_animation_frames(self, pattern_name: str, frames: int = 8) -> List[List[List[int]]]:
        """
        Create animation frames by rotating a pattern
        
        Args:
            pattern_name: Name of the base pattern
            frames: Number of animation frames
            
        Returns:
            List of pattern matrices
        """
        base_pattern = self.get_pattern(pattern_name)
        if not base_pattern:
            return []
        
        animation = []
        for i in range(frames):
            # Rotate pattern
            rotated = np.rot90(np.array(base_pattern), i)
            animation.append(rotated.tolist())
        
        return animation

def main():
    """Demo the pattern generator"""
    generator = LEDPatternGenerator()
    
    print("Available patterns:", generator.list_patterns())
    
    # Create and display some patterns
    patterns_to_show = ['smiley', 'heart', 'star', 'spiral']
    
    for pattern_name in patterns_to_show:
        pattern = generator.get_pattern(pattern_name)
        if pattern:
            print(f"\n{pattern_name.upper()} pattern:")
            for row in pattern:
                print(' '.join('█' if bit else ' ' for bit in row))
            
            # Convert to Arduino format
            arduino_bytes = generator.convert_to_arduino_bytes(pattern)
            print(f"Arduino bytes: {arduino_bytes}")
    
    # Create custom pattern
    custom_points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]
    custom_pattern = generator.create_custom_pattern(custom_points)
    print("\nCustom diagonal pattern:")
    for row in custom_pattern:
        print(' '.join('█' if bit else ' ' for bit in row))

if __name__ == "__main__":
    main()
