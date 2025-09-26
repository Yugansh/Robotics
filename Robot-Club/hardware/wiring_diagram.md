# Wiring Diagram for Cardboard Robot

## Arduino Pin Connections

### Servo Motors
- **Left Servo (Movement)**: Digital Pin 9
- **Right Servo (Movement)**: Digital Pin 10
- **Servo Power**: 5V
- **Servo Ground**: GND

### LED Matrix (MAX7219)
- **VCC**: 5V
- **GND**: GND
- **DIN**: Digital Pin 11
- **CS**: Digital Pin 10
- **CLK**: Digital Pin 13

### Power
- **9V Battery**: Connected to Arduino VIN pin
- **Ground**: Common ground for all components

## Circuit Layout

```
Arduino Uno/Nano
├── Pin 9  → Left Servo Signal (Orange/Yellow wire)
├── Pin 10 → Right Servo Signal (Orange/Yellow wire)
├── Pin 11 → LED Matrix DIN
├── Pin 12 → LED Matrix CS
├── Pin 13 → LED Matrix CLK
├── 5V     → Servo Power (Red wires) + LED Matrix VCC
└── GND    → All Ground connections (Black/Brown wires)
```

## LED Matrix Connection Details

The MAX7219 LED matrix typically comes with these pins:
- **VCC** (Power) → Arduino 5V
- **GND** (Ground) → Arduino GND
- **DIN** (Data In) → Arduino Pin 11
- **CS** (Chip Select) → Arduino Pin 12
- **CLK** (Clock) → Arduino Pin 13

## Servo Motor Connections

Each servo motor has three wires:
- **Red** → 5V (Power)
- **Black/Brown** → GND (Ground)
- **Orange/Yellow** → Signal pin (PWM)

## Power Considerations

- **Arduino**: Can be powered via USB or 9V battery
- **Servos**: Require 5V, can be powered from Arduino's 5V pin
- **LED Matrix**: Requires 5V, can be powered from Arduino's 5V pin
- **Total Current**: Ensure 9V battery can provide at least 1A

## Safety Notes

1. **Double-check connections** before powering on
2. **Use proper polarity** for all components
3. **Don't exceed voltage ratings** (5V for servos and LED matrix)
4. **Secure all connections** to prevent shorts
5. **Test each component** individually before full assembly

## Troubleshooting

### Common Issues
- **Servos not moving**: Check power and signal connections
- **LED matrix not working**: Verify DIN, CS, CLK connections
- **Arduino not responding**: Check power and USB connection
- **Erratic behavior**: Check for loose connections

### Testing Steps
1. Upload basic Arduino sketch
2. Test servos with simple movement commands
3. Test LED matrix with basic pattern
4. Test full integration
