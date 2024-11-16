# Space Invaders Game using Pygame

## Project Overview
This project is a Python-based Space Invaders game developed using the **Pygame** library. It is designed as a learning tool to demonstrate key Object-Oriented Programming (OOP) concepts such as classes, objects, inheritance, and polymorphism. The game follows the traditional Space Invaders format where the player controls a spaceship to shoot down aliens and survive as long as possible.

The game illustrates the practical application of OOP principles in programming, such as structuring the game components as objects and using classes to manage various elements like the player, aliens, bullets, and levels.

### Key Features:
- **Multiple Levels**: Different difficulty levels including Easy, Normal, and Hard.
- **Alien Invasion**: Multiple alien enemies with varying behaviors and speeds.
- **Shooting Mechanism**: The player can shoot bullets to destroy aliens.
- **Game Over and Leaderboard**: Displays a Game Over screen and stores the highest scores.
- **OOP Design**: The game is structured using OOP principles, with multiple classes for different game entities like the player, aliens, bullets, and levels.

### Objective:
The goal of this game is to demonstrate the use of OOP in developing a full-fledged game, allowing students to grasp key concepts of classes, methods, inheritance, and object management in a dynamic and interactive environment.

---

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Game Structure](#game-structure)
4. [Algorithm Explanation](#algorithm-explanation)
5. [Dependencies](#dependencies)
6. [File Structure](#file-structure)
7. [Future Enhancements](#future-enhancements)

---

## Installation

To run the Space Invaders game on your local machine, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Methasit-Pun/Game-UI.git
   cd Game-UI
   ```

2. **Install Python and Pygame**:

   Make sure you have Python 3 installed on your system. You can install Pygame using the following command:

   ```bash
   pip install pygame
   ```

---

## Usage

1. To start the game, run the `main.py` script:

   ```bash
   python main.py
   ```

2. The game will start, displaying the main menu where you can choose to start a new game or view the leaderboard.
3. Use the arrow keys to move the spaceship and the spacebar to shoot.
4. Try to survive as long as possible and achieve the highest score!

---

## Game Structure

The game is broken down into various classes, each handling a specific part of the game:

1. **Main Game Loop (`main.py`)**:
   - Controls the game flow, including starting the game, switching between menus, and updating the game state.

2. **Player Class**:
   - Manages the player's spaceship, including movement and shooting.
   - Inherits from a common `GameObject` class that provides basic properties like position and image.

3. **Alien Class**:
   - Represents the alien enemies, handles their movement and collision detection.
   - Inherits from the `GameObject` class.

4. **Bullet Class**:
   - Represents the player's bullets, handles their movement and collision detection.

5. **Levels (`easy_level.py`, `normal_level.py`, `hard_level.py`)**:
   - Manages the difficulty of the game, adjusting alien speed and number based on the chosen level.

6. **Game Over & Leaderboard (`gameover.py`, `leaderboard.py`)**:
   - Displays the game-over screen and tracks high scores.

7. **Button Class (`button.py`)**:
   - Handles all the buttons in the menu, including functionality to start the game, quit, or navigate the leaderboard.

---

## Algorithm Explanation

1. **Main Loop**:
   - The game loop continuously updates the game state, including moving the player, firing bullets, and checking for collisions with aliens.
   
2. **Collision Detection**:
   - The program checks for collisions between bullets and aliens, and when a collision is detected, the corresponding alien is removed, and the player's score is incremented.

3. **Level Progression**:
   - As the player progresses through the game, the level of difficulty increases by speeding up the aliens and introducing more of them.

4. **Game Over**:
   - When the player’s spaceship is hit by an alien, the game ends, and the final score is saved in the leaderboard.

---

## Dependencies

The following Python libraries are required to run the game:

- **Pygame**: For rendering graphics and handling user input.
  
To install the dependencies, run:

```bash
pip install pygame
```

---

## File Structure

The project is organized as follows:

```
space-invaders/
│
├── assets/                         # Folder containing images and sound assets (e.g., BG.jpg, Alien.mp3)
│
├── img/                            # Folder for game images (e.g., player spaceship, aliens)
│
├── button.py                       # Handles buttons in the game menu
├── easy_level.py                   # Easy level settings and behavior
├── gameover.py                     # Game over screen and functionality
├── hard_level.py                   # Hard level settings and behavior
├── main.py                         # Main game loop and initialization
├── normal_level.py                 # Normal level settings and behavior
├── tempCodeRunnerFile.py           # Temporary file generated during development
├── __pycache__/                    # Python bytecode files (generated automatically)
├── README.md                       # Project documentation
└── .idea/                          # IDE project files (if using an IDE like PyCharm)
```

---

## Future Enhancements

- **Multiplayer Mode**: Add a feature to allow two players to play the game simultaneously.
- **Power-ups**: Introduce power-ups such as shields, faster bullets, or special bombs.
- **Advanced AI**: Enhance the alien AI to create more challenging and unpredictable movements.
- **Graphics and Animations**: Improve game graphics and animations to make the game more visually appealing.

---

## Credits
This project was developed as part of the **Programming Methodology** subject in Year 2, Semester 2 at **Chulalongkorn University**. The game was built using **Pygame** and follows the principles of **Object-Oriented Programming (OOP)**.

---

Feel free to modify and expand this README based on the specifics of your project.
