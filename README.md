
---

# Chess Game Overview

This project is a simple chess game built using [Python](https://www.python.org/) and the [Pygame](https://www.pygame.org/docs/) library. It allows you to play chess against another player on the same computer. Below is a brief explanation of how the game works and its main features.

## Features

- **Graphical Chess Board**: The game displays an 8x8 chess board with alternating beige and brown squares, just like a real chess board.
- **Piece Movement**: You can click and drag pieces to move them around the board. The game enforces the rules of chess, so you can only make legal moves.
- **Undo Move**: If you make a mistake, you can press the 'Z' key to undo your last move.
- **Chess Notation**: Each move is printed in standard [chess notation] (https://en.wikipedia.org/wiki/Chess_notation), helping you keep track of the game.
- **Responsive Design**: The game adjusts the size of the pieces and board based on the window size.

## How It Works

1. **Setup**: The game initializes by loading images for each chess piece and setting up the board.
2. **Game Loop**: The main loop of the game listens for events like mouse clicks and key presses.
   - **Mouse Clicks**: Clicking on a piece selects it, and dragging it to a new square attempts to make a move.
   - **Key Presses**: Pressing 'Z' undoes the last move.
3. **Drawing**: The board and pieces are drawn on the screen, updating with each move.
4. **Game State**: The game keeps track of the current state, including whose turn it is and what moves are valid.

## Getting Started

To play the game, you'll need to have [Python](https://www.python.org/) and [Pygame](https://www.pygame.org/docs/) installed on your computer. Once you have those set up, you can run the game by executing the main script.

---

        
