import chess
from core import ChessDetector

class Board:
    
    def __init__(self):
        self.board = chess.Board()
        # Set up the default,rest of the pieces...
        ChessDetector.set_default_locations(self)
   
    def update_board(self, piece_locations):
        self.board.clear()
        # Map the detected piece locations to squares on the board
        for piece, location in piece_locations.items():
            x, y = location
            square = chess.square(x, y)
            piece_type = self.get_chess_piece_type(piece)
            color = self.get_chess_piece_color(piece)
            chess_piece = chess.Piece(piece_type, color)
            self.board.set_piece_at(square, chess_piece)

    def get_chess_piece_type(self, piece):

        piece_map = {
            'king'   : chess.KING,
            'queen'  : chess.QUEEN,
            'bishop1': chess.BISHOP,
            'bishop2': chess.BISHOP,
            'knight1': chess.KNIGHT,
            'knight2': chess.KNIGHT,
            'rook1'  : chess.ROOK,
            'rook2'  : chess.ROOK,
            'pawn1'  : chess.PAWN,
            'pawn2'  : chess.PAWN,
            'pawn3'  : chess.PAWN,
            'pawn4'  : chess.PAWN,
            'pawn5'  : chess.PAWN,
            'pawn6'  : chess.PAWN,
            'pawn7'  : chess.PAWN,
            'pawn8'  : chess.PAWN,
        }

        return piece_map.get(piece, chess.PAWN)
        
        
