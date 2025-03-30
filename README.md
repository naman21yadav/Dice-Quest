# Dice Quest

## Overview

Dice Quest is a fun, interactive game where players roll 2-6 dice multiple times in each game. The objective is to achieve a victory by ensuring the median value is the same as the mean value in the list of dice roll results.

## How to Play

1. **Start the Game** - Choose the number of dice (between 2 and 6) and the type of dice (6, 8, or 9-sided).
2. **Roll the Dice** - The game rolls the selected dice type and displays the results.
3. **Check Win/Loss** - After multiple rolls, the game determines if the player wins (if the mean equals the median) or loses.
4. **View Game History** - Players can check their game history, including the number of dice used, rounds played, and win/loss status.

## Features

- Allows rolling multiple dice with different types (6, 8, or 9-sided)
- Uses ASCII art to visually display dice rolls
- Tracks game history
- Determines win or loss based on statistical calculations

## Installation

1. Clone the repository or download `dice.py`.
2. Ensure you have Python installed (recommended: Python 3+).
3. Run the game using:
   ```bash
   python dice.py
   ```

## Dependencies

- Python standard library (no external dependencies required)

## Game Flow

1. The game starts with a Main Menu that provides options:

- Start Game
- View Game History
- Exit

2. In the Game Menu, the player selects:

- Number of dice
- Type of dice
- Roll dice
- Check win/loss status

3. The game calculates the win/loss status and stores game history.

## Example

    Welcome to ROLL DICE GAME

    Options:
    1: Start game
    2: Game History
    3: EXIT

## Author

Developed by Naman Yadav
