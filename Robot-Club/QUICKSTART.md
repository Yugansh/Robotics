# Quick Start Guide

## Getting Started in 5 Minutes

### 1. Hardware Setup
1. **Gather materials** from `hardware/parts_list.md`
2. **Follow assembly guide** in `hardware/assembly_guide.md`
3. **Connect electronics** according to `hardware/wiring_diagram.md`

### 2. Software Setup
1. **Install Arduino IDE** and upload `arduino/cardboard_robot.ino`
2. **Install Python dependencies**:
   ```bash
   cd python
   pip install -r requirements.txt
   ```

### 3. Test Your Robot
1. **Run basic movement test**:
   ```bash
   python examples/basic_movement.py
   ```

2. **Test LED patterns**:
   ```bash
   python examples/led_patterns.py
   ```

3. **Try drawing demo**:
   ```bash
   python examples/drawing_demo.py
   ```

### 4. Start Programming
```python
from python.robot_controller import CardboardRobot

robot = CardboardRobot()
robot.connect()
robot.move_forward()
robot.display_pattern('heart')
robot.disconnect()
```

## Troubleshooting

### Robot Won't Move
- Check servo connections
- Verify power supply
- Test Arduino code upload

### LED Matrix Not Working
- Check DIN, CS, CLK connections
- Verify WS2812B wiring
- Test with simple pattern

### Python Connection Issues
- Check serial port (Windows: COM3, Mac/Linux: /dev/ttyUSB0)
- Ensure Arduino is connected
- Try different baud rates

## Next Steps

1. **Customize patterns** in `python/pattern_generator.py`
2. **Add sensors** for obstacle detection
3. **Create your own movements** and sequences
4. **Decorate your robot** with paint and accessories

## Need Help?

- Check the full documentation in `README.md`
- Review assembly instructions in `hardware/`
- Try the example programs in `examples/`
- Experiment with the interactive modes

Happy building! 🤖✨
