import chess
from core import ChessDetector

class Board:
    def __init__(self):
        self.board = chess.Board()

    def initialize_board(self):
      ChessDetector.set_default_locations(self)
        # Set up the rest of the pieces...
        
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
            'king': chess.KING,
            'queen': chess.QUEEN,
            'bishop1': chess.BISHOP,
            'bishop2': chess.BISHOP,
            'knight1': chess.KNIGHT,
            'knight2': chess.KNIGHT,
            'rook1': chess.ROOK,
            'rook2': chess.ROOK,
            'pawn1': chess.PAWN,
            'pawn2': chess.PAWN,
        }
        return piece_map.get(piece, chess.PAWN)
        
    def get_chess_piece_color(self, piece):
        if self.player_color == 'white':
            if piece == 'king' or piece.startswith('rook') or piece.startswith('pawn'):
                return chess.WHITE
            else:
                return chess.BLACK
        else:
            if piece == 'king' or piece.startswith('rook') or piece.startswith('pawn'):
                return chess.BLACK
            else:
                return chess.WHITE
