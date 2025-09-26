# Visual Design of the Final Cardboard Robot

## Overall Robot Specifications
- **Total Height**: 140-150cm
- **Total Width**: 80cm (at torso)
- **Total Depth**: 60cm (at torso)
- **Weight**: Approximately 15-20kg

## ASCII Art Representation

```
                    ┌─────────────────┐
                    │   EARS (15cm)   │  ← Team 7: Speaker Ears
                    │   🔊     🔊     │
                    └─────────────────┘
                           │
                    ┌─────────────────┐
                    │  EYES (12cm)    │  ← Team 8: LED Eyes
                    │  👁️     👁️     │
                    └─────────────────┘
                           │
        ┌─────────────────────────────────┐
        │        HEAD MODULE              │  ← Team 1: Head
        │     (40cm x 30cm x 30cm)        │
        │  ┌─────────────────────────┐    │
        │  │   LED MATRIX (16x16)    │    │
        │  │   ████████████████      │    │
        │  │   ██  ██  ██  ██        │    │
        │  │   ████████████████      │    │
        │  │   ██  ██  ██  ██        │    │
        │  └─────────────────────────┘    │
        └─────────────────────────────────┘
                           │
        ┌─────────────────────────────────┐
        │        TORSO MODULE             │  ← Team 2: Torso
        │     (60cm x 40cm x 50cm)        │
        │  ┌─────────────────────────┐    │
        │  │   BATTERY COMPARTMENT   │    │
        │  │   (12V 7Ah Battery)     │    │
        │  └─────────────────────────┘    │
        │  ┌─────────────────────────┐    │
        │  │   SERVO CONTROL         │    │
        │  │   CIRCUITS              │    │
        │  └─────────────────────────┘    │
        └─────────────────────────────────┘
           │                           │
    ┌─────────────┐               ┌─────────────┐
    │ LEFT ARM    │               │ RIGHT ARM   │  ← Teams 3 & 4: Arms
    │ (50cm long) │               │ (50cm long) │
    │ ┌─────────┐ │               │ ┌─────────┐ │
    │ │ SHOULDER│ │               │ │ SHOULDER│ │
    │ └─────────┘ │               │ └─────────┘ │
    │ ┌─────────┐ │               │ ┌─────────┐ │
    │ │  ELBOW  │ │               │ │  ELBOW  │ │
    │ └─────────┘ │               │ └─────────┘ │
    │ ┌─────────┐ │               │ ┌─────────┐ │
    │ │  HAND   │ │               │ │  HAND   │ │
    │ └─────────┘ │               │ └─────────┘ │
    └─────────────┘               └─────────────┘
           │                           │
    ┌─────────────┐               ┌─────────────┐
    │ LEFT LEG    │               │ RIGHT LEG   │  ← Teams 5 & 6: Legs
    │ (60cm long) │               │ (60cm long) │
    │ ┌─────────┐ │               │ ┌─────────┐ │
    │ │   HIP   │ │               │ │   HIP   │ │
    │ └─────────┘ │               │ └─────────┘ │
    │ ┌─────────┐ │               │ ┌─────────┐ │
    │ │  KNEE   │ │               │ │  KNEE   │ │
    │ └─────────┘ │               │ └─────────┘ │
    │ ┌─────────┐ │               │ ┌─────────┐ │
    │ │  FOOT   │ │               │ │  FOOT   │ │
    │ │  ⚫⚫⚫   │ │               │ │  ⚫⚫⚫   │ │  ← Wheels (30cm)
    │ └─────────┘ │               │ └─────────┘ │
    └─────────────┘               └─────────────┘
```

## Detailed Module Views

### Head Module (Front View)
```
┌─────────────────────────────────┐
│  EARS: 🔊 (15cm x 10cm x 8cm)   │
│  ┌─────────────────────────────┐ │
│  │  EYES: 👁️ (12cm x 8cm x 6cm)│ │
│  │  ┌─────────────────────────┐ │ │
│  │  │  LED MATRIX (16x16)     │ │ │
│  │  │  ████████████████       │ │ │
│  │  │  ██  ██  ██  ██         │ │ │
│  │  │  ████████████████       │ │ │
│  │  │  ██  ██  ██  ██         │ │ │
│  │  │  ████████████████       │ │ │
│  │  │  ██  ██  ██  ██         │ │ │
│  │  │  ████████████████       │ │ │
│  │  │  ██  ██  ██  ██         │ │ │
│  │  └─────────────────────────┘ │ │
│  └─────────────────────────────┘ │
└─────────────────────────────────┘
```

### Torso Module (Side View)
```
┌─────────────────────────────────┐
│  ┌─────────────────────────────┐ │
│  │  BATTERY COMPARTMENT        │ │
│  │  (12V 7Ah)                  │ │
│  └─────────────────────────────┘ │
│  ┌─────────────────────────────┐ │
│  │  SERVO CONTROL CIRCUITS     │ │
│  │  (Arduino Mega)             │ │
│  └─────────────────────────────┘ │
│  ┌─────────────────────────────┐ │
│  │  POWER DISTRIBUTION         │ │
│  │  HUB                        │ │
│  └─────────────────────────────┘ │
└─────────────────────────────────┘
```

### Arm Module (Side View)
```
┌─────────────────────────────────┐
│  SHOULDER JOINT                 │
│  ┌─────────────────────────────┐ │
│  │  UPPER ARM (30cm)           │ │
│  │  ┌─────────────────────────┐ │ │
│  │  │  SERVO MOTOR (MG996R)   │ │ │
│  │  └─────────────────────────┘ │ │
│  └─────────────────────────────┘ │
│  ELBOW JOINT                     │
│  ┌─────────────────────────────┐ │
│  │  LOWER ARM (20cm)           │ │
│  └─────────────────────────────┘ │
│  WRIST JOINT                     │
│  ┌─────────────────────────────┐ │
│  │  HAND (10cm)                │ │
│  └─────────────────────────────┘ │
└─────────────────────────────────┘
```

### Leg Module (Side View)
```
┌─────────────────────────────────┐
│  HIP JOINT                      │
│  ┌─────────────────────────────┐ │
│  │  THIGH (30cm)               │ │
│  │  ┌─────────────────────────┐ │ │
│  │  │  SERVO MOTOR (MG996R)   │ │ │
│  │  └─────────────────────────┘ │ │
│  └─────────────────────────────┘ │
│  KNEE JOINT                      │
│  ┌─────────────────────────────┐ │
│  │  SHIN (20cm)                │ │
│  └─────────────────────────────┘ │
│  ANKLE JOINT                     │
│  ┌─────────────────────────────┐ │
│  │  FOOT (25cm)                │ │
│  │  ┌─────────────────────────┐ │ │
│  │  │  WHEEL (30cm diameter)  │ │ │
│  │  │  ⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫ │ │ │
│  │  └─────────────────────────┘ │ │
│  └─────────────────────────────┘ │
└─────────────────────────────────┘
```

## Color Scheme and Materials

### Cardboard Colors
- **Head**: White/light gray cardboard
- **Torso**: Dark gray/black cardboard
- **Arms**: Medium gray cardboard
- **Legs**: Dark gray/black cardboard
- **Ears**: Light gray cardboard
- **Eyes**: White/transparent acrylic

### LED Colors
- **Head LED Matrix**: RGB (full color)
- **Eyes**: RGB (full color)
- **Status Indicators**: Red/Green/Blue

### Decorative Elements
- **Eyes**: Glowing LED strips with diffuser
- **Ears**: Speaker grilles with ventilation
- **Arms**: Joint covers and decorative panels
- **Legs**: Wheel covers and traction elements
- **Torso**: Access panels and ventilation

## Functional Features

### Movement Capabilities
- **Head**: LED matrix display, eye animations
- **Arms**: 3-joint articulation (shoulder, elbow, wrist)
- **Legs**: 3-joint articulation (hip, knee, ankle)
- **Wheels**: 30cm diameter for movement

### Interactive Features
- **LED Matrix**: 16x16 display for patterns and text
- **Eyes**: Animated LED strips for expressions
- **Ears**: Audio output for sound effects
- **Movement**: Coordinated servo control

### Power and Control
- **Battery**: 12V 7Ah for extended operation
- **Control**: Arduino Mega for complex control
- **Communication**: Serial interface for programming
- **Safety**: Emergency stop and safety systems

## Assembly Sequence Visualization

### Phase 1: Base Assembly
```
    ┌─────────────┐
    │ LEFT LEG    │
    │ ⚫⚫⚫        │
    └─────────────┘
           │
    ┌─────────────────┐
    │   TORSO MODULE  │
    └─────────────────┘
           │
    ┌─────────────┐
    │ RIGHT LEG   │
    │        ⚫⚫⚫ │
    └─────────────┘
```

### Phase 2: Upper Body
```
    ┌─────────────┐
    │ LEFT ARM    │
    └─────────────┘
           │
    ┌─────────────────┐
    │   TORSO MODULE  │
    └─────────────────┘
           │
    ┌─────────────┐
    │ RIGHT ARM   │
    └─────────────┘
```

### Phase 3: Head Assembly
```
    ┌─────────────────┐
    │   HEAD MODULE   │
    │  ┌─────────────┐│
    │  │ LED MATRIX  ││
    │  └─────────────┘│
    └─────────────────┘
           │
    ┌─────────────────┐
    │   TORSO MODULE  │
    └─────────────────┘
```

### Phase 4: Facial Features
```
    ┌─────────────────┐
    │  EARS: 🔊   🔊   │
    │  EYES: 👁️   👁️   │
    │  ┌─────────────┐│
    │  │ LED MATRIX  ││
    │  └─────────────┘│
    └─────────────────┘
```

## Final Robot Specifications

### Dimensions
- **Height**: 140-150cm
- **Width**: 80cm (torso)
- **Depth**: 60cm (torso)
- **Weight**: 15-20kg

### Electronics
- **Arduino Mega 2560**: Main controller
- **4x Servo Motors**: Movement control
- **16x16 LED Matrix**: Display
- **2x LED Strips**: Eye animations
- **2x Speakers**: Audio output
- **12V 7Ah Battery**: Power source

### Materials
- **Heavy-duty cardboard**: Main structure
- **Wooden dowels**: Structural support
- **Metal brackets**: Joint connections
- **Acrylic sheets**: LED protection
- **Rubber strips**: Wheel traction

This visual design shows the complete modular robot with all components, dimensions, and assembly sequence!
