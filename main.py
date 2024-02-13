# This is under develompent...
# So,.. it not complated yet...
# ...
from core import chess_detector
import cv2
import numpy
from Analyze import chess_engine

def main():
    webcam = cv2.VideoCapture(0)
    piece_weights_path = "<path_to_yolov5_weights>"

    chess_detector = ChessDetector(piece_weights_path)
    board = Board()
    board.initialize_board()

    while True:
        ret, frame = webcam.read()

        chess_detector.detect_chessboard(frame)
        chess_detector.detect_pieces(frame)

        #Updating board:
        board.update_board(chess_detector.piece_locations)
        # ... Perform analysis or any other tasks using the updated board ...

        cv2.imshow("Chess Detection", frame)

        if chess_detector.player_color is None:
            chess_detector.set_player_color()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    webcam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()