# Convoy 

### ChessEngine Breakdown
- **Initialization (`__init__` method):** 
  - Initializes an 8x8 chess board with pieces in their starting positions.
  - Sets `white_to_move` to `True`, indicating it's white's turn to move.
  - Initializes `move_log` to keep track of all moves made, which is useful for undoing moves.

- **`undo_move` Method:**
  - Reverts the last move made by popping it from `move_log`.
  - Restores the piece to its original position and captures back any piece that was taken.
  - Switches the turn back to the previous player.

- **`getValidMoves` Method:**
  - Placeholder for generating all valid moves, considering checks and other rules. Currently, it calls `getAllPossibleMoves`, which does not consider checks.

- **`getAllPossibleMoves` Method:**
  - Iterates over the board to find all possible moves for the current player, without considering checks.
  - Calls specific methods to get moves for pawns and rooks (`getPawnMoves` and `getRookMoves`), though these methods are not yet implemented.

- **`make_move` Method:**
  - Executes a move by updating the board and logging the move.
  - Switches the turn to the other player.

### `Move` Class
- **Initialization (`__init__` method):**
  - Takes starting and ending positions and the board as input.
  - Stores the starting and ending row and column indices.
  - Records the piece being moved and any piece being captured.
  - Generates a unique `moveID` for the move, useful for comparison.

- **`__eq__` Method:**
  - Overrides the equality operator to compare moves based on their `moveID`.

- **`get_chess_notation` Method:**
  - Converts the move into standard chess notation using file (column) and rank (row) labels.

### Additional Notes
- The code is structured to handle basic chess operations but lacks implementations for special moves like castling, en passant, and pawn promotion.
- The `getPawnMoves` and `getRookMoves` methods are placeholders and need to be implemented to generate actual moves for these pieces.
- The `getValidMoves` method is intended to filter out moves that would leave the king in check, but this logic is not yet implemented.

### ChessEngine Breakdown 

### Imports and Constants
- **Imports**: The script imports necessary modules, including `os` for file path operations, `pygame` as `p` for game development, and `ChessEngine` for handling the game logic.
- **Constants**: 
  - `WIDTH` and `HEIGHT` define the dimensions of the game window.
  - `DIMENSION` is set to 8, representing an 8x8 chess board.
  - `SQ_SIZE` calculates the size of each square on the board.
  - `MAX_FPS` sets the frame rate for the game loop.
  - `IMAGES` is a dictionary to store loaded images of chess pieces.
  - `BEIGE` and `BROWN` are colors used for the chess board squares.

### Image Loading
- **`loadImages()` Function**: This function loads and scales images for each chess piece. It iterates over a list of piece identifiers (e.g., "wp" for white pawn) and loads the corresponding image file from the `images` directory, scaling it to fit the square size.

### Main Game Loop
- **`main()` Function**: This is the main driver function for the chess game.
  - Initializes Pygame and sets up the display window.
  - Creates a `GameState` object from the `ChessEngine` module to manage the game state.
  - Loads images and initializes a font for drawing text on the board.
  - Initializes variables for tracking selected squares and player clicks.
  - Retrieves valid moves from the game state and sets a flag (`moveMade`) to track when a move is made.

- **Event Handling**:
  - **Mouse Events**:
    - `MOUSEBUTTONDOWN`: Captures the position of the mouse click and determines if a piece is being selected for dragging.
    - `MOUSEBUTTONUP`: Captures the position where the mouse button is released, constructs a move, and checks if it's valid. If valid, the move is executed, and the dragging state is reset.
  - **Keyboard Events**:
    - `KEYDOWN`: Checks for specific key presses, such as the 'Z' key to undo the last move.

- **Move Handling**:
  - If a move is made, the list of valid moves is updated.
  - The game state is drawn on the screen, and the display is updated at the specified frame rate.

### Drawing Functions
- **`drawGameState()`**: Draws the current state of the game, including the board and pieces.
- **`drawBoard()`**: Draws the chess board with alternating colors for squares and calls `drawBoardLabels()` to add file and rank labels.
- **`drawBoardLabels()`**: Adds labels to the board for files (a-h) and ranks (1-8).
- **`drawPieces()`**: Iterates over the board and draws each piece in its respective position using the loaded images.
- **`drawDraggingPiece()`**: Draws the piece currently being dragged by the player, following the mouse cursor.

### Execution
- The script checks if it is being run as the main module and calls the `main()` function to start the game.

### Notes
- **ChessEngine Module**: The script relies on the `ChessEngine` module to handle game logic, such as move validation and execution. This module should define classes and methods like `GameState`, `Move`, `getValidMoves()`, `make_move()`, and `undo_move()`.
- **Images and Fonts**: Ensure that the images for chess pieces are stored in the `images` directory and that the font file `Roboto-Regular.ttf` is available in the working directory.

This code provides a basic framework for a chess game, handling user interactions through mouse and keyboard events, and rendering the game state using Pygame's drawing capabilities.

