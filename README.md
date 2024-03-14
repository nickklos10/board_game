# Treasure Hunt Game Project

### Introduction

This Python script simulates a treasure hunt game where players move around a game board to collect treasures and potentially engage in combat with other players using weapons. 
The game incorporates elements of randomness, strategy, and interaction among players within a specified game board.

### Key Components

**Game Initialization**

1. The game board's width and height are set based on user input.
2. A specified number of players are added to the game, each placed at random positions on the board.
3. Treasures and weapons are scattered across the board at random locations, each with its own properties like point value or strike distance.

**Classes and Their Functions**

- **Game:** Manages the game's state, including players, treasures, and weapons. It contains methods to handle player movements,
  interactions with game objects, and the game's progression until a winning condition is met.
- **Player:** Represents a player in the game, tracking their position, collected treasures, weapons, and energy points.
- **Treasure:** Represents a treasure object on the game board, with attributes like name, symbol, point value, and position.
- **Weapon:** Represents a weapon object that players can collect and use, with attributes including name, symbol, strike distance, and position.
- **Randomnum:** Represents a custom random number generator, influencing the game's dynamics by determining the initial positions of players, treasures, and weapons on the game board.

### Gameplay Mechanics

- Players take turns deciding whether to move or rest. Moving decreases energy, and resting increases it.
- Players can collect treasures to gain points and weapons to eliminate other players.
- The game continues until all treasures are collected or only one player remains.
- Players' movements and interactions are based on user input for each turn.

## How to Run the Script

1. **Running the Main Script:** Navigate to the directory containing your game files in a terminal or command prompt.
   Run the main.py file, which is designed to tie all the components together and execute the game logic:

   python main.py

2. **Gameplay:** Follow the on-screen instructions to make choices for each player during their turn.
   Players can choose to move in a specified direction and distance or to rest and regain energy.
   The game updates the board and player statuses after each turn, showing collected treasures and player eliminations.

3. **End of the Game:** The game concludes when one player remains or all treasures are collected.
   The winner is the player with the highest points from collected treasures.
