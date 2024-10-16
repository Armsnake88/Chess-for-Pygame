
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
        self.white_to_move = True #False is black
        self.move_log = []

    def undo_move(self):
        if len(self.move_log) != 0:
            move = self.move_log.pop()
            self.board[move.start_row][move.start_col] = move.piece_moved
            self.board[move.end_row][move.end_col] = move.piece_captured
            self.white_to_move = not self.white_to_move
    ''' 
    Get all possible moves 
    Check all possible moves for opponent 
    See what moves expose the king 
    Validate the move if it does not leave the king under attack 
    return valid moves only
    '''
    def getValidMoves(self):
        return self.getAllPossibleMoves() #ignoring checks for now



    ''' 
    All moves without considering checks
    '''
    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == 'w' and self.white_to_move) and (turn == 'b' and not self.white_to_move):
                    piece = self.board[r][c][1]
                    if piece == 'p':
                        self.getPawnMoves(r,c, moves)
                    elif piece == 'R':
                        self.getRookMoves(r, c, moves)
        return moves
    ''' 
    gets all pawn moves based on piece position
    '''
    def getPawnMoves(self, r, c, moves):
        pass
    def getRookMoves(self, r, c, moves):
        pass







    ''' 
make_move takes Move as a parameter to execute it  
special moves like en passant, castling etc. won't be addressed here
    '''
    def make_move(self, move):  # start here if you're having errors with piece's being set to empty
        self.board[move.start_row][move.start_col] = "--" #leaves the sq the piece started on blank
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.move_log.append(move)  # Logs the move so we can undo it later
        self.white_to_move = not self.white_to_move





class Move:
    def __init__(self, start_pos, end_pos, board):
        self.start_row = start_pos[0]
        self.start_col = start_pos[1]
        self.end_row = end_pos[0]
        self.end_col = end_pos[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]
        self.moveID = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col
        print(self.moveID)

''' 
Overrides equals method
'''
def __eq__(self,other):
    if isinstance(other,Move):
        return self.moveID == other.moveID
    return False



def get_chess_notation(self):
        files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        ranks = ['1', '2', '3', '4', '5', '6', '7', '8']
        return f"{files[self.start_col]}{ranks[7 - self.start_row]},{files[self.end_col]}{ranks[7 - self.end_row]}"