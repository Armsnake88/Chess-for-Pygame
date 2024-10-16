
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

1. **Imports and Setup**:
   - The script starts by importing necessary libraries: `os` for operating system interactions, `pygame` for game development, and a custom `ChessEngine` module for handling the chess game logic.
   - Constants are defined for the game window size, chessboard dimensions, square size, and colors for the board.

2. **Loading Images**:
   - A function `loadImages()` loads images of chess pieces from a directory and scales them to fit the board squares. These images are stored in a dictionary for easy access during the game.

3. **Main Game Loop**:
   - The `main()` function is the core of the game. It initializes Pygame, sets up the game window, and prepares the game state.
   - It enters a loop that continues running until the player quits the game. Within this loop, it handles events like mouse clicks and key presses.

4. **Handling Mouse Events**:
   - When the player clicks on a piece, the game records the piece and its position.
   - When the player releases the mouse button, the game calculates the new position and checks if the move is valid. If valid, it updates the game state.

5. **Handling Key Events**:
   - If the player presses the 'Z' key, the game undoes the last move.

6. **Drawing the Game**:
   - The game continuously updates the display to show the current state of the board and pieces.
   - Functions like `drawGameState()`, `drawBoard()`, `drawPieces()`, and `drawDraggingPiece()` handle the visual representation of the board, pieces, and any piece being dragged by the player.

7. **Game State Management**:
   - The game uses a `GameState` object from the `ChessEngine` module to manage the rules and logic of chess, such as valid moves and move history.

8. **Exiting the Game**:
   - The game loop exits when the player closes the window, and Pygame is properly shut down.

Overall, this script sets up a basic interactive chess game where players can click and drag pieces to make moves, with the game logic ensuring that only legal moves are allowed. 

---

        
