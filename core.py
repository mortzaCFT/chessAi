# CORE_VERSION : "0.0.0.0"

# =--=
# Whats new:
# Generally removing some functions, that they wasn't nessecery.
# Also some editing in deteting chess_board and the chess_pieces.
# The algorithm of the program changes. Now we just detect grid of the chess_board.
# We are no longer using yolov5 anymore.It's doesnt req with new algorithm.
# =--=
# Suggestion for updating:
# Let user fix any pieces the simple detector gets wrong. It's will help for any bug(since we have changed the algorithm)
# Infer the piece locations from the board state history.
# Limit pieces to pre-defined regions. Detect the board grid, define regions like "white pieces must be in rows 1-2"
# 
# =--=
# Creator : mortzaCFT
# Address : https://github.com/mortzaCFT
# Discord : mortza#3700 

import cv2
import numpy as np
import chess

class ChessDetector:
    
    def __init__(self):
        self.chessboard_corners = None
        self.piece_locations = {}

    #Detecting,... board.
    def detect_chessboard(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        ret, corners = cv2.findChessboardCorners(gray, (8, 8), None)

        if ret:
            self.chessboard_corners = corners
            # Divide the chessboard into cells (rectangles)
            cell_width = int(corners[1][0][0] - corners[0][0][0])
            cell_height = int(corners[8][0][1] - corners[0][0][1])
            grid_cells = []
            for i in range(8):
                for j in range(8):
                    x1 = int(corners[i * 8 + j][0][0])
                    y1 = int(corners[i * 8 + j][0][1])
                    x2 = x1 + cell_width
                    y2 = y1 + cell_height
                    grid_cells.append(((x1, y1), (x2, y2)))

            return grid_cells
        else:
            return None

    
    #Set up the board 
    def set_default_locations(self):
        #For player color white:
        if self.player_color == 'white': 
         self.piece_locations['king']    = (4, 0)
         self.piece_locations['queen']   = (3, 0)
         self.piece_locations['bishop1'] = (2, 0)
         self.piece_locations['bishop2'] = (6, 0)
         self.piece_locations['knight1'] = (1, 0)
         self.piece_locations['knight2'] = (5, 0)
         self.piece_locations['rook1']   = (0, 0)
         self.piece_locations['rook2']   = (7, 0)
         for i in range(8):
             self.piece_locations[f'pawn{i+1}'] = (i, 1)
        #For player color black:
        if self.player_color == 'black':
         self.piece_locations['king']    = (4, 7)
         self.piece_locations['queen']   = (3, 7)
         self.piece_locations['bishop1'] = (2, 7)
         self.piece_locations['bishop2'] = (6, 7)
         self.piece_locations['knight1'] = (2, 7)
         self.piece_locations['knight2'] = (5, 7)
         self.piece_locations['rook1']   = (0, 7)
         self.piece_locations['rook2']   = (7, 7)
         for ii in range(8):
             self.piece_locations[f'pawn{ii+1}'] = (ii, 6)
    
    def set_color(self):
        while True:
            try:
                color = input("Enter your chess piece color (white/black): ").lower() 
                if color not in ['white', 'black']:
                    raise ValueError("Invalid input! Please enter 'white' or 'black'.")
                self.player_color = color
                if color == 'white':
                    self.enemy_color = 'black'
                else:
                    self.enemy_color = 'white' 
                break
            except ValueError as e:
                print(e)

    def get_chess_piece_type(self, piece_locations):

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

        return piece_map.get(piece_locations, chess.PAWN)


# Updating location of the chess pieces
def update_board(self, grid_cells):
    #Set up that shit board.
    self.board = chess.Board()

    # Create a dictionary to store the mapped square for each piece
    piece_squares = {}

    # Set default piece locations first before overriding with detections
    self.set_default_locations()

    for piece, location in self.piece_locations.items():
        x, y = location

        # Find the grid cell containing the piece
        for cell in grid_cells:
            (x1, y1), (x2, y2) = cell
            if x1 <= x <= x2 and y1 <= y <= y2:
                square = chess.square(x, y)
                piece_type = self.get_chess_piece_type(piece)

                # Store the mapped square for the piece
                piece_squares[piece] = square
                break

    # Deploy player pieces in real time
    player_color_int = chess.WHITE if self.player_color == 'white' else chess.BLACK
    for piece, square in piece_squares.items():
        piece_type = self.get_chess_piece_type(piece)
        player_chess_piece = chess.Piece(piece_type, player_color_int)
        self.board.set_piece_at(square, player_chess_piece)

    # Deploy enemy pieces in real time
    enemy_color_int = chess.BLACK if self.player_color == 'white' else chess.WHITE
    for enemy_piece, enemy_location in self.enemy_piece_locations.items():
        enemy_x, enemy_y = enemy_location

        if enemy_piece in piece_squares:
            # Remove the player piece from its mapped square
            enemy_square = piece_squares[enemy_piece]
            self.board.remove_piece_at(enemy_square)
        else:
            enemy_square = chess.square(enemy_x, enemy_y)

        enemy_piece_type = self.get_chess_piece_type(enemy_piece)
        enemy_chess_piece = chess.Piece(enemy_piece_type, enemy_color_int)
        self.board.set_piece_at(enemy_square, enemy_chess_piece)

     #Old one=---------------------------------------------------------------------------
     #self.board = chess.Board()
     #self.set_default_locations()

     #for piece, location in self.piece_locations.items():
      #  x, y = location
       # square = chess.square(x, y)
        #piece_type = self.get_chess_piece_type(piece)

        #Deploy real time the player piece 
        #player_color_int = chess.WHITE if self.player_color == 'white' else chess.BLACK
        #for piece, location in self.piece_locations.items():
         # player_chess_piece = chess.Piece(piece_type, player_color_int)
          #self.board.set_piece_at(square,player_chess_piece)


        #Deploy real time the player piece 
        #enemy_color_int = chess.BLACK if self.player_color == 'white' else chess.WHITE
        #for piece, location in self.enemy_piece_locations.items():
         # enemy_chess_piece = chess.Piece(piece_type, enemy_color_int)
          #self.board.set_piece_at(square, enemy_chess_piece) 
    #-------------------------------------------------------------------------------------
