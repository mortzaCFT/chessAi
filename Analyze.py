# This script is under development:
# This class can connect the chess_engine and the main applicaion,
#in order for get suggestion from xboard or UCI chess engines.
#The algorithm is seems simple,but it's don't working(i don't know enough informaion,...)

from Board import Board
from core import chess_detector
from main import main

class chess_engine:
 
 
 def analyze_and_suggest(engine, board, time_limit_ms):

#We are using xboard for now.
    engine.set_position(board.fen())  # Convert board to FEN string
    result = engine.command('bestmove')
    best_move_san = result['move']

   #.............................................................................
 # For UCI protocol
     # if isinstance(engine, uci.engine):  
     #   response = engine.info()
     #   best_move_uci = response['pv'][0]  # Extract the best move from principal variation
     #  best_move_san = chess.san(best_move_uci)  # Convert UCI move to SAN
     #............................................................................
    #---------------------------------------------------------------------------------------------------------
 # Perform additional analysis or filtering if needed (e.g., legal moves, filtering based on player skill)
   #---------------------------------------------------------------------------------------------------------  
    
    # Determine the rectangle targeted by the best move
    # (assuming board squares start at (0, 0) in top-left corner)
    initial_file, initial_rank = chess.parse_square(best_move_san)[0]
    target_file, target_rank = chess.parse_square(best_move_san)[1]
    initial_rectangle = (initial_file, initial_rank)
    target_rectangle = (target_file, target_rank)



  #   The best move is returned in Standard Algebraic Notation (SAN) format, like "c3" or "Nf3". This is a human-readable representation commonly used in chess notation.
   #    To identify the rectangular location of the move, we can convert the SAN move to coordinates (file, rank) using methods like chess.parse_square(best_move_san).
    #    Based on these coordinates, ywe can target and highlight the appropriate rectangle on the chessboard visualization in our application.
    return best_move_san, initial_rectangle, target_rectangle
