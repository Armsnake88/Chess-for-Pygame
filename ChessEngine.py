class GameState:
    def __init__(self):
        '''
        Board is an 8x8 2D list
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
        self.white_to_move = True  # True if it's white's turn
        self.move_log = []

    def undo_move(self):
        if len(self.move_log) != 0:
            move = self.move_log.pop()
            self.board[move.start_row][move.start_col] = move.piece_moved
            self.board[move.end_row][move.end_col] = move.piece_captured
            self.white_to_move = not self.white_to_move

    def getValidMoves(self):
        # This should include logic to check for checks
        return self.getAllPossibleMoves()  # ignoring checks for now

    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == 'w' and self.white_to_move) or (turn == 'b' and not self.white_to_move):
                    piece = self.board[r][c]  # Get the full piece string
                    if piece == 'wp':  # White Pawn
                        self.getPawnMoves(r, c, moves)
                    elif piece == 'bp':  # Black Pawn
                        self.getPawnMoves(r, c, moves)
                    elif piece == 'wN':  # White Knight
                        self.getKnightMoves(r, c, moves)
                    elif piece == 'bN':  # Black Knight
                        self.getKnightMoves(r, c, moves)
                    elif piece == 'wB':  # White Bishop
                        self.getBishopMoves(r, c, moves)
                    elif piece == 'bB':  # Black Bishop
                        self.getBishopMoves(r, c, moves)
                    elif piece == 'wR':  # White Rook
                        self.getRookMoves(r, c, moves)
                    elif piece == 'bR':  # Black Rook
                        self.getRookMoves(r, c, moves)
                    elif piece == 'wQ':  # White Queen
                        self.getQueenMoves(r, c, moves)
                    elif piece == 'bQ':  # Black Queen
                        self.getQueenMoves(r, c, moves)
                    elif piece == 'wK':  # White King
                        self.getKingMoves(r, c, moves)
                    elif piece == 'bK':  # Black King
                        self.getKingMoves(r, c, moves)
        return moves

    def getPawnMoves(self, r, c, moves):
        if self.white_to_move:  # for white pawns
            if r > 0 and self.board[r - 1][c] == "--":  # Move forward
                moves.append(Move((r, c), (r - 1, c), self.board))
                if r == 6 and self.board[r - 2][c] == "--":  # Double move from starting position
                    moves.append(Move((r, c), (r - 2, c), self.board))

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
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        enemy_color = 'b' if self.white_to_move else 'w'
        for d in directions:
            for i in range(1, 8):
                end_row = r + d[0] * i
                end_col = c + d[1] * i
                if 0 <= end_row < 8 and 0 <= end_col < 8:  # Check if on board
                    end_piece = self.board[end_row][end_col]
                    if end_piece == "--":  # Empty square
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                    elif end_piece[0] == enemy_color:  # Enemy piece
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                        break
                    else:  # Friendly piece
                        break
                else:
                    break

    def getQueenMoves(self, r, c, moves):
        self.getRookMoves(r, c, moves)  # Queen moves like a rook
        self.getBishopMoves(r, c, moves)  # Queen moves like a bishop

    def getKnightMoves(self, r, c, moves):
        knight_moves = [
            (-2, -1), (-1, -2), (1, -2), (2, -1),
            (2, 1), (1, 2), (-1, 2), (-2, 1)
        ]
        ally_color = 'w' if self.white_to_move else 'b'
        for m in knight_moves:
            end_row = r + m[0]
            end_col = c + m[1]
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                end_piece = self.board[end_row][end_col]
                if end_piece[0] != ally_color:
                    moves.append(Move((r, c), (end_row, end_col), self.board))

    def getKingMoves(self, r, c, moves):
        king_moves = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        ally_color = 'w' if self.white_to_move else 'b'
        for i in range(8):
            end_row = r + king_moves[i][0]
            end_col = c + king_moves[i][1]
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                end_piece = self.board[end_row][end_col]
                if end_piece[0] != ally_color:
                    moves.append(Move((r, c), (end_row, end_col), self.board))

    def getBishopMoves(self, r, c, moves):
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonal directions
        enemy_color = 'b' if self.white_to_move else 'w'
        for d in directions:
            for i in range(1, 8):
                end_row = r + d[0] * i
                end_col = c + d[1] * i
                if 0 <= end_row < 8 and 0 <= end_col < 8:
                    end_piece = self.board[end_row][end_col]
                    if end_piece == "--":
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                    elif end_piece[0] == enemy_color:
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                        break
                    else:
                        break
                else:
                    break

    def make_move(self, move):
        # Check if the move is valid
        valid_moves = self.getValidMoves()
        if move in valid_moves:
            # Execute the move
            self.board[move.start_row][move.start_col] = "--"  # Empty the start square
            self.board[move.end_row][move.end_col] = move.piece_moved
            self.move_log.append(move)
            self.white_to_move = not self.white_to_move  # Toggle turn

            # Handle special moves (e.g., promotion)
            if move.piece_moved[1] == 'P' and (move.end_row == 0 or move.end_row == 7):
                self.board[move.end_row][move.end_col] = move.piece_moved[0] + 'Q'  # Promote to queen


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
        return f"({files[self.start_col]}{ranks[7 - self.start_row]},{files[self.end_col]}{ranks[7 - self.end_row]})"

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False
