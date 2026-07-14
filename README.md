#ESP32 Engineering Projects Portfolio

Welcome to my ESP32 Engineering Projects repository!

This repository showcases embedded systems projects that I independently designed, programmed, assembled and tested using the **ESP32** and **MicroPython**. These projects were created to strengthen my understanding of electronics, programming and hardware-software integration.
---

#About Me

Hi! I'm **Adarsh Das**, an O-Level student with a strong interest in Electrical & Electronic Engineering and Computer Engineering.
My interest in engineering began with experimenting with electronics and has grown through studying O-Level Computing, participating in coding competitions, and independently learning embedded systems using the ESP32.

Through these projects, I developed practical skills in:

- Embedded Systems
- MicroPython Programming
- Circuit Prototyping
- GPIO Programming
- I²C Communication
- Hardware Troubleshooting
- Problem Solving
- Engineering Design

---

# Projects

## Project 1 – ESP32 Reaction Time Tester

### Overview

A reaction time testing game built using an ESP32, SSD1306 OLED display and push button.

The game measures how quickly a user reacts after a randomly generated "GO!" signal and records the fastest reaction time during the session.

---

### Features :

- OLED menu interface
- Press button to start
- 3...2...1 countdown
- Random delay before "GO!"
- Measures reaction time in milliseconds
- False start detection
- Displays current reaction time
- Displays fastest reaction time

---

### Hardware Used :

- ESP32 Development Board
- SSD1306 128×64 OLED Display (I²C)
- Push Button
- Breadboard
- Jumper Wires

---

### 🔌 Wiring

#### OLED

| OLED | ESP32 |
|------|--------|
| GND | GND |
| VCC | 3.3V |
| SDA | GPIO21 |
| SCL | GPIO22 |

#### Push Button

| Button | ESP32 |
|---------|--------|
| One Side | GPIO4 |
| Other Side | GND |

The button uses the ESP32's internal pull-up resistor (`Pin.PULL_UP`), so no external resistor is required.

---

### How It Works :

1. Press the button to start the game.
2. A 3...2...1 countdown begins.
3. The ESP32 waits a random amount of time.
4. "GO!" appears.
5. The user's reaction time is measured.
6. The OLED displays:
   - Current reaction time
   - Best reaction time

If the button is pressed before "GO!" appears, the game displays **"Too Early!"** and resets.

---

### Skills Demonstrated :

- Embedded Systems
- ESP32 Programming
- GPIO Programming
- I²C Communication
- OLED Display Control
- Digital Inputs
- Circuit Prototyping
- Debugging
- Troubleshooting

---

### Challenges Faced :

One challenge was that the OLED initially could not communicate with the ESP32. By using an I²C scanner, I identified that the problem was related to the hardware connection and corrected the wiring by replacing the male to male cables to female to female cables as i did not have much female to male cables

Another challenge involved the push button, which initially remained in a constant logic state due to incorrect wiring. By testing GPIO inputs and understanding the button's internal connections, I corrected the circuit.

---

### Future Improvements:

- Save high score permanently in flash memory
- Add buzzer sound effects
- Multiple difficulty levels
- OLED animations
- Wi-Fi leaderboard

---

## Project 2 – ESP32 Smart Motion Detection Counter

### Overview

A motion detection counter built using an ESP32, PIR motion sensor and SSD1306 OLED display.

Whenever movement is detected, the ESP32 increases a motion counter and displays the updated count on the OLED screen.

This project demonstrates how sensors can be integrated with microcontrollers to process real-time inputs.

---

### Features :

- PIR motion detection
- Live motion counter
- OLED display
- Real-time updates
- Compact embedded system

---

### Hardware Used :

- ESP32 Development Board
- PIR Motion Sensor
- SSD1306 OLED Display
- Breadboard
- Jumper Wires

---

### Wiring :

#### PIR Sensor

| PIR | ESP32 |
|------|--------|
| VCC | 3.3V |
| GND | GND |
| OUT | GPIO (Configured in code) |

#### OLED

| OLED | ESP32 |
|------|--------|
| GND | GND |
| VCC | 3.3V |
| SDA | GPIO21 |
| SCL | GPIO22 |

---

### How It Works :

1. The PIR sensor continuously monitors for movement.
2. When motion is detected, it outputs a HIGH signal.
3. The ESP32 detects the signal through a GPIO pin.
4. The motion counter increases.
5. The OLED updates the display.

---

### Skills Demonstrated :

- Embedded Systems
- ESP32 Programming
- PIR Motion Sensors
- Digital Inputs
- GPIO Programming
- I²C Communication
- OLED Displays
- Circuit Design
- Debugging

---

### Challenges Faced :

One challenge was ensuring that repeated movement was counted accurately without multiple counts from a single detection. Through testing and refining the program logic, I improved the reliability of the counter.

Another challenge involved integrating the PIR sensor and OLED display simultaneously while ensuring both devices communicated correctly with the ESP32.

---

### Possible Applications :

- Smart Homes
- Visitor Counters
- Security Systems
- Room Occupancy Monitoring
- Automatic Lighting Systems

---

### Future Improvements :

- Store motion count permanently
- Cloud dashboard using Wi-Fi
- Mobile notifications
- Time and date logging
- Battery-powered operation

---

# Technologies Used

## Programming

- MicroPython
- Python

## Hardware

- ESP32
- SSD1306 OLED Display
- PIR Motion Sensor
- Push Button
- Breadboard
- Jumper Wires

## Engineering Concepts

- Embedded Systems
- GPIO Programming
- Digital Inputs
- I²C Communication
- Circuit Prototyping
- Debugging
- Hardware Troubleshooting

---

# What I Learned

Through building these projects, I gained practical experience in integrating hardware and software while developing systematic troubleshooting skills.

I learnt how to:

- Build and test electronic circuits
- Read sensor inputs using GPIO
- Communicate with peripherals using I²C
- Design interactive embedded applications
- Debug both hardware and software issues
- Improve projects through testing and iteration

These projects strengthened my passion for Electrical & Electronic Engineering and Computer Engineering, motivating me to continue exploring embedded systems and intelligent technologies.

---

# Future Goals

Moving forward, I hope to develop more advanced embedded systems by incorporating:

- Internet of Things (IoT)
- Wireless communication
- Data logging
- Mobile applications
- Robotics
- Artificial Intelligence

My long-term goal is to design innovative engineering solutions that combine electronics and software to solve real-world problems.

---

# Author

**Adarsh Das**

O-Level Computing Student

Aspiring Electrical & Electronic / Computer Engineer
