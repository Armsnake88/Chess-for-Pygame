

class GameState:
    def __init__(self):
        '''
        Board is a 8x8 2d list
        '''
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]
        self.white_to_move = True  # False is black
        self.move_log = []

    def undo_move(self):
        if len(self.move_log) != 0:
            move = self.move_log.pop()
            self.board[move.start_row][move.start_col] = move.piece_moved
            self.board[move.end_row][move.end_col] = move.piece_captured
            self.white_to_move = not self.white_to_move

    def getValidMoves(self):
        return self.getAllPossibleMoves()  # ignoring checks for now

    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == 'w' and self.white_to_move) or (turn == 'b' and not self.white_to_move):
                    piece = self.board[r][c][1]

                    if piece == 'p':
                        self.getPawnMoves(r, c, moves)
                    elif piece == 'R':
                        self.getRookMoves(r, c, moves)
        return moves

    def getPawnMoves(self, r, c, moves):
        if self.white_to_move:  # for white pawns
            if r > 0 and self.board[r - 1][c] == "--":  # Move forward
                moves.append(Move((r, c), (r - 1, c), self.board))
                if r == 6 and self.board[r - 2][c] == "--":  # Double move from starting position
                    moves.append(Move((r, c), (r - 2, c), self.board))
            '''  
            Remember: r and c represent the current index for a piece.
            For white pawns, moving "forward" means moving to a lower row number  
            they start from higher row numbers and move towards row 0.   
            ^ For black pawns, it means moving to a higher row number
            r > 0 and c > 0 keeps the pieces within the board when moving 
            '''
            # Captures
            if c > 0 and self.board[r - 1][c - 1][0] == 'b':  # Capture left
                moves.append(Move((r, c), (r - 1, c - 1), self.board))
            if c < len(self.board[r]) - 1 and self.board[r - 1][c + 1][0] == 'b':  # Capture right
                moves.append(Move((r, c), (r - 1, c + 1), self.board))

            # En passant
            # Add logic for en passant here

        else:  # for black pawns
            if r < len(self.board) - 1 and self.board[r + 1][c] == "--":  # Move forward
                moves.append(Move((r, c), (r + 1, c), self.board))
                if r == 1 and self.board[r + 2][c] == "--":  # Double move from starting position
                    moves.append(Move((r, c), (r + 2, c), self.board))

            # Captures
            if c > 0 and self.board[r + 1][c - 1][0] == 'w':  # Capture left
                moves.append(Move((r, c), (r + 1, c - 1), self.board))
            if c < len(self.board[r]) - 1 and self.board[r + 1][c + 1][0] == 'w':  # Capture right
                moves.append(Move((r, c), (r + 1, c + 1), self.board))

            # En passant
            # Add logic for en passant here

    def getRookMoves(self, r, c, moves):

        pass
    def getQueenMoves(self, r, c, moves):
        pass
    def getKnightMoves(self, r, c, moves):
        pass
    def getKingMoves(self, r, c, moves):
        pass
    def getBishopMoves(self, r, c, moves):
        pass

    def make_move(self, move):
        # Generate all valid moves
        valid_moves = self.getValidMoves()

        # Check if the move is valid
        if move in valid_moves:
            # Execute the move
            self.board[move.start_row][move.start_col] = "--"  # Empty the start square
            self.board[move.end_row][move.end_col] = move.piece_moved
            self.white_to_move = not self.white_to_move
            self.move_log.append(move)



class Move:
    def __init__(self, start_pos, end_pos, board):
        self.start_row = start_pos[0]
        self.start_col = start_pos[1]
        self.end_row = end_pos[0]
        self.end_col = end_pos[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]
        self.moveID = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col


    def get_chess_notation(self):
        files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        ranks = ['1', '2', '3', '4', '5', '6', '7', '8']
        return f"{files[self.start_col]}{ranks[7 - self.start_row]},{files[self.end_col]}{ranks[7 - self.end_row]}"

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False
