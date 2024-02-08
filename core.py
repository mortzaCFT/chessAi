#  Core detecton using yolov5.
#  This is simply get all needed objects in a board.
import cv2
import numpy as np
import torch
from Board import Board

class ChessDetector:
   
    def __init__(self, piece_weights_path):
        self.piece_weights_path = piece_weights_path
        self.chessboard_corners = None
        self.piece_locations = {}
        self.player_color = None
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=self.piece_weights_path)

    def detect_chessboard(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, (8, 8), None)
        if ret:
            self.chessboard_corners = corners

    def detect_pieces(self, frame):
        
        img = letterbox(frame, new_shape=self.model.img_size)

        results = self.model(img)

        
        labels = results.pandas().xyxy[0]['name']
        boxes = results.pandas().xyxy[0][['xmin', 'ymin', 'xmax', 'ymax']]

        known_pieces = set(['king', 'queen', 'bishop', 'knight', 'rook', 'pawn'])
        # Assign the piece names to the piece_locations dictionary
        for label, box in zip(labels, boxes):
            xmin, ymin, xmax, ymax = box
            piece_name = label

            if piece_name in known_pieces:
                self.piece_locations[piece_name] = (xmin, ymin, xmax, ymax)

    def set_default_locations(self):
        # Set the default locations for the chess pieces
        self.piece_locations['king'] = (4, 0)
        self.piece_locations['queen'] = (3, 0)
        self.piece_locations['bishop1'] = (2, 0)
        self.piece_locations['bishop2'] = (5, 0)
        self.piece_locations['knight1'] = (1, 0)
        self.piece_locations['knight2'] = (6, 0)
        self.piece_locations['rook1'] = (0, 0)
        self.piece_locations['rook2'] = (7, 0)
        for i in range(8):
            self.piece_locations[f'pawn{i+1}'] = (i, 1)

    def set_player_color(self):
        while True:
            try:
                color = input("Enter your chess piece color (white/black): ").lower()
                if color not in ['white', 'black']:
                    raise ValueError("Invalid input! Please enter 'white' or 'black'.")
                self.player_color = color
                break
            except ValueError as e:
                print(e)

if __name__ == "__main__":
    webcam = cv2.VideoCapture(0)  
    
    # Load the YOLOv5 model
    # path the weghts of yolov5...
    piece_weights_path = "<path_to_yolov5_weights>"
    chess_detector = ChessDetector(piece_weights_path)
    
    while True:
        ret, frame = webcam.read()  
        
        chess_detector.detect_chessboard(frame)  
        chess_detector.detect_pieces(frame)  
        cv2.imshow("Chess Detection", frame)
        
        
        if chess_detector.player_color is None:
            chess_detector.set_player_color()  
        
        Board.initialize_board()
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):  
            break
    
    webcam.release()
    cv2.destroyAllWindows()
