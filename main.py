# This is under develompent...
# So,.. it not complated yet...
# ...
from core import ChessDetector
import cv2
import numpy
from Analyze import chess_engine


def main():

    webcam = cv2.VideoCapture(0)  
    
    core = ChessDetector()
    core.set_color()  
    
    while True:
        ret, frame = webcam.read()  
        cv2.imshow("Chess Detection", frame)
        
        #Setting up the board :
        grid_cells = core.detect_chessboard(frame)

        #Getting output:
        if grid_cells is not None:
          print(f"Detected {len(grid_cells)} grid cells.")
          core.update_board(grid_cells)  # Pass grid_cells here
        else:
           print("Chessboard not detected.")

        #Comminicate with stockfish...
        #Getting respound from stockfish:


        # This proces can break the loop:
        if cv2.waitKey(1) & 0xFF == ord('q'):  
            break
    
    webcam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
   
