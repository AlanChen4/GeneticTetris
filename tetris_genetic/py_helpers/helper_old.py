import cv2
import json
import time

from copy import deepcopy

from py_helpers import pieces

class Heuristics:
    ''' gathers the heuristics for the lua AI'''

    def __init__(self):
        while True:
            updated_status = self.update_board(console = False)

            # wait for status to update and then get next move
            if updated_status:
                self.get_decision()

                # sleep value prevents get_decision from being called twice
                time.sleep(0.5)
                

    def convert_image(self):
        '''converts fceux screenshot to a black and white grid'''
        try:
            status_image = cv2.imread("game_state/status.png")
            cropped_image = status_image[40:200, 95:175]
            colored_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
            final_image = cv2.resize(colored_image, (10, 22))

            cv2.imwrite('game_state/converted_image.png', final_image)
        except TypeError:
            # TypeError is raised when status.png has not been created
            pass


    def update_board(self, console):
        '''updates the status image and prints to console'''
        if self.get_game_status() == 2:
            
            self.convert_image()

            # converts the image into an array
            self.board = []
            converted_image = cv2.imread('game_state/converted_image.png')
            
            for row in range(22):
                for col in range(10):
                    # add new row every ten spots
                    if col % 10 == 0:
                        self.board.append([])
                    # '.' for empty, '#' for filled spots
                    if converted_image[row][col][0] == 0:
                        self.board[row].append('.')
                    else:
                        self.board[row].append('#')

            # clears command prompt and prints array in readable format
            if console:
                print("\n"*30)
                for row in self.board:
                    print(row)

            return True


    def get_height(self, board):
        ''' returns the total height of the board'''
        aggregate_height = 0
        for row in range(22):
            for col in range(10):
                if board[row][col] == '#':
                    aggregate_height+=1
        return aggregate_height


    def get_lines_cleared(self, board):
        '''returns the total number of complete lines'''
        lines_cleared = 0
        for row in range(22):
            cleared_line = True
            for spot in board[row]:
                if spot[0] == '.':
                    cleared_line = False
            if cleared_line:
                lines_cleared+=1
        return lines_cleared


    def get_holes(self, board):
        '''returns the number of empty spaces with a tile above it'''
        number_of_holes = 0
        for row in range(22):
            for spot_index, spot in enumerate(board[row]):
                # not exactly sure why it's 21 instead of 22
                if row > 0:
                    # checks if there is empty space and spot above is a piece
                    if board[row-1][spot_index] == '#':
                        if board[row][spot_index] == '.':
                            number_of_holes+=1
        return number_of_holes


    def get_bumps(self, board):
        bumpiness = 0

        # determine the individual heights of each column
        col_heights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for row in range(22):
            for col in range(10):
                if board[row][col] == '#':
                    col_heights[col] += 1

        # formula for "bumpiness"
        for i in range(0, 10, 2):
            bumpiness += abs(col_heights[i] - col_heights[i-1])

        return bumpiness


    def get_game_status(self):
        ''' returns current status of game from RAM map'''
        game_status = open('game_state/fceux_status.txt', 'r')
        game_status = game_status.read()
        try:
            game_status_number = int(game_status)
        except ValueError:
            game_status_number = 0
        return game_status_number


    def get_decision(self):
        '''makes decision on the best move based on score function'''

        # fetch piece first
        piece = pieces.get_piece(console = False)
 
        # place piece will record score values to hypo_scores
        self.hypo_scores = []

        # go through each piece spot and rotation and record score values
        for x in range(10 - len(piece[0])):
            for rotation in range(4):
                self.place_piece(x, piece, rotation)

        # get the highest score from hypo_scores
        highest_score = -100000
        highest_score_index = None
        for score_index, score in enumerate(self.hypo_scores):
            if score['score'] > highest_score:
                highest_score = score['score']
                highest_score_index = score_index

        best_board = self.hypo_scores[highest_score_index]['board']
        print('score:', self.hypo_scores[highest_score_index]['score'])
        print('x-value:', self.hypo_scores[highest_score_index]['x_value'])
        print('rotations:', self.hypo_scores[highest_score_index]['rotations'])
        for r in best_board:
            print(r)


    def place_piece(self, x, piece, rotate_times):
        '''drops piece in hypothetical board and returns the hypothetical board, hypo_board'''

        hypo_board = deepcopy(self.board)
        piece = pieces.rotate_piece(piece, rotate_times)
        piece_length = len(piece[0])

        for row_index in range(22):

            # reached the bottom
            if row_index == 21:
                for row_p_index, row_piece in enumerate(piece):
                    for spot_index, spot_piece in enumerate(row_piece):
                        row_value = (22-len(piece))+row_p_index
                        if hypo_board[row_value][x+spot_index] == '.':
                            hypo_board[row_value][x+spot_index] = spot_piece 
                break

            # piece confliction
            elif '#' in hypo_board[row_index+1]:
                # determine is there are any pieces in conflict
                is_piece = False
                for piece_row_index, piece_row in enumerate(piece):
                    for spot_index, spot_value in enumerate(piece_row):
                        if spot_value == '#':
                            if hypo_board[row_index-((len(piece)-2)-piece_row_index)][spot_index+x] == '#':
                                is_piece = True
                if is_piece:
                    for piece_row_index, piece_row in enumerate(piece):
                        for spot_index, spot_value in enumerate(piece_row):
                            if hypo_board[(row_index-len(piece))+piece_row_index+1][spot_index+x] == '.':
                                hypo_board[(row_index-len(piece))+piece_row_index+1][spot_index+x] = spot_value
                    break

        


