# Task 2 – Tic-Tac-Toe AI

## Project Overview

This project is a Python-based Tic-Tac-Toe game where a human player competes against an AI opponent.

The AI uses game logic to analyze the available positions and select a suitable move. The project demonstrates basic Artificial Intelligence concepts, decision making, and Python programming.

## Features

* Human vs AI gameplay
* 3 × 3 Tic-Tac-Toe board
* AI opponent
* Win detection
* Draw detection
* Input validation
* Command-line interface
* Replayable game

## Technologies Used

* Python 3
* Artificial Intelligence
* Game Logic
* Minimax Algorithm

## Project Structure

```text
task2_tictactoe_ai/
│
├── tictactoe_ai.py
└── README.md
```

## How to Run

### 1. Install Python

Make sure Python 3 is installed.

Check the Python version:

```bash
python --version
```

### 2. Open the Project Folder

```bash
cd task2_tictactoe_ai
```

### 3. Run the Program

```bash
python tictactoe_ai.py
```

## How to Play

* The human player uses `X`.
* The AI uses `O`.
* The board contains 9 positions.
* Enter the position number to place your symbol.
* The first player to get three symbols in a row wins.
* If all positions are filled without a winner, the game is a draw.

## Game Board

```text
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```

For example, entering `5` places your symbol in the center.

## AI Working

The AI checks the current board and evaluates the possible moves.

The basic process is:

```text
Current Board
      ↓
Find Available Moves
      ↓
Evaluate Possible Moves
      ↓
Select Best Move
      ↓
AI Makes Move
      ↓
Check Winner
```

The Minimax approach can be used to evaluate possible future moves and select an appropriate move for the AI.

## Sample Output

```text
Welcome to Tic-Tac-Toe AI!

You are X
AI is O

  |   |  
-----------
  |   |  
-----------
  |   |  

Enter your move (1-9): 5

AI is thinking...

  | O |  
-----------
  | X |  
-----------
  |   |  

Enter your move (1-9):
```

The game continues until the player wins, the AI wins, or the game ends in a draw.

## Learning Outcomes

Through this project, I learned:

* Python programming
* Game development logic
* Artificial Intelligence fundamentals
* Decision-making techniques
* Minimax algorithm
* Functions and conditional statements
* User input handling
* Problem-solving skills

## Future Enhancements

* Add a graphical user interface using Tkinter
* Add Easy, Medium, and Hard difficulty levels
* Add score tracking
* Add two-player mode
* Add sound effects
* Develop a web-based version
* Improve the AI strategy

## Author

**Aretty Neha**

Computer Science and Engineering Student

GitHub: https://github.com/ArettyNeha17

## Internship Task

**Task 2:** Tic-Tac-Toe AI

**Status:** Completed ✅

**Technology:** Python

## Acknowledgement

This project was developed as part of my internship task to gain practical experience in Python programming and Artificial Intelligence.
