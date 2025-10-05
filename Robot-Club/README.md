# Large Cardboard Robot with LED Matrix Drawing (140-150cm)

A DIY large-scale cardboard-based robot that combines mechanical movement with LED matrix drawing capabilities. This project uses Arduino Mega for hardware control and Python for high-level programming and pattern generation.

## Features

- **Mechanical Movement**: 4x high-torque servo motors for precise movement control
- **LED Matrix Drawing**: 16x16 LED matrix for displaying large patterns and drawings
- **Large Cardboard Construction**: Eco-friendly and easily customizable design (140-150cm height)
- **Python Interface**: Easy-to-use Python API for programming the robot
- **Arduino Control**: Reliable hardware control with Arduino Mega

## Project Structure

```
Robot-Club/
├── README.md                 # This file
├── arduino/                  # Arduino code
│   ├── cardboard_robot.ino   # Main Arduino sketch
│   └── libraries/            # Required Arduino libraries
├── python/                   # Python control interface
│   ├── robot_controller.py   # Main Python controller
│   ├── pattern_generator.py  # LED pattern generation
│   └── requirements.txt      # Python dependencies
├── hardware/                 # Hardware documentation
│   ├── parts_list.md         # Complete parts list
│   ├── wiring_diagram.md     # Circuit connections
│   └── assembly_guide.md     # Step-by-step assembly
└── examples/                 # Example programs
    ├── basic_movement.py     # Basic movement examples
    ├── led_patterns.py       # LED pattern examples
    └── drawing_demo.py       # Drawing demonstration
```

## Quick Start

1. **Hardware Setup**: Follow the assembly guide in `hardware/assembly_guide.md`
2. **Arduino Setup**: Upload `arduino/cardboard_robot.ino` to your Arduino
3. **Python Setup**: Install dependencies with `pip install -r python/requirements.txt`
4. **Run Examples**: Try the example programs in the `examples/` directory

## Hardware Requirements

- Arduino Mega 2560
- 4x High-torque servo motors (MG996R)
- 16x16 LED matrix (WS2812B or similar)
- Heavy-duty cardboard sheets (100cm x 150cm)
- Wooden dowels and structural support
- Jumper wires
- Large breadboard
- 12V 7Ah battery and connector
- Heavy-duty tools (craft knife, long ruler, wood glue)

## Software Requirements

- Arduino IDE
- Python 3.7+
- Required Python packages (see `python/requirements.txt`)

## Getting Started

1. Clone or download this repository
2. Follow the assembly instructions
3. Upload the Arduino code
4. Install Python dependencies
5. Run the example programs

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project!

## License

This project is open source and available under the MIT License.
