# Wire Loop Game
A physical wire loop game that uses a Raspberry Pi 2 to handle game logic.

## Overview

I developed this project in high school as part of a mentorship program with an industry software engineer. 

The game's goal is simple: guide a copper wand along a copper track from one end to another, and if you touch the track three times, the game ends.

This project granted me hands-on experience with integrating hardware and software through basic circuitry and embedded programming, and it served as a great introduction to the field of computer engineering.

## Implementation
To construct this project, the following hardware parts were used:
- Raspberry Pi 2
- Breadboard
- Copper wire (for track and wand)
- Wooden block
- 3.5mm speaker (audio feedback)

The software component of the project was developed in Python using PyCharm, which handles GPIO input for contact events, stores the number of touches, and ends the game after three detected contacts.
