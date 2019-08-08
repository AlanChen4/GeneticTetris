import cv2
import json
import time

from py_helpers import pieces

class Heuristics:
    ''' gathers the heuristics for the lua AI'''


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


    def update_board(self, debug):
        '''updates the status image and prints to console'''
        try:
            game_status = open('game_state/fceux_status.txt', 'r')
            game_status = int(game_status.read())
        except ValueError:
            pass
        # this game_status threshold is one value lower in order to
        # provide time for calculations before update_info is called
        if game_status == 2:
            self.convert_image()

            if debug:
                # delay for debugging purposes
                time.sleep(0.5)

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
            
            if debug:
                # clears command prompt and prints array in tetris format
                print("\n"*30)
                for row in self.board:
                    print(row)


    def get_height(self):
        ''' returns the total height of the board'''
        aggregate_height = 0
        for row in range(22):
            for col in range(10):
                if self.board[row][col] == '#':
                    aggregate_height+=1
        return aggregate_height


    def get_lines_cleared(self):
        '''returns the total number of complete lines'''
        lines_cleared = 0
        for row in range(22):
            cleared_line = True
            for spot in self.board[row]:
                if spot[0] == '.':
                    cleared_line = False
            if cleared_line:
                lines_cleared+=1
        return lines_cleared


    def get_holes(self):
        '''returns the number of empty spaces with a tile above it'''
        number_of_holes = 0
        for row in range(22):
            for spot_index, spot in enumerate(self.board[row]):
                # not exactly sure why it's 21 instead of 22
                if row > 0:
                    # checks if there is empty space and spot above is a piece
                    if self.board[row-1][spot_index] == '#':
                        if self.board[row][spot_index] == '.':
                            number_of_holes+=1
        return number_of_holes


    def get_bumps(self):
        bumpiness = 0

        # determine the individual heights of each column
        col_heights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for row in range(22):
            for col in range(10):
                if self.board[row][col] == '#':
                    col_heights[col] += 1

        # formula for "bumpiness"
        for i in range(0, 10, 2):
            bumpiness += abs(col_heights[i] - col_heights[i-1])

        return bumpiness


    def update_info(self, spacing=False):
        '''prints heuristics to the console'''
        if spacing:
            print("\n"*20)
            time.sleep(0.1)

        game_status = open('game_state/fceux_status.txt', 'r')
        game_status = game_status.read()

        # only perform actions if game_status is greater than 1 
        try:
            self.game_status_number = int(game_status)
        except ValueError:
            self.game_status_number = 0
        if self.game_status_number == 3:
            height = self.get_height()
            lines_cleared = self.get_lines_cleared()
            holes = self.get_holes()
            bumps = self.get_bumps()
            

            with open ('game_state/game_status.json') as file:
                info = json.load(file)
                info['height'] = height
                info['lines_cleared'] = lines_cleared
                info['holes'] = holes
                info['bumps'] = bumps

            with open('game_state/game_status.json', 'w') as file:
                json.dump(info, file)      

            # this sleep delays keeps too many print messages from being displayed
            time.sleep(0.1)

            print("----------")
            print("aggregate height: {}".format(height))
            print("lines cleared: {}".format(lines_cleared))
            print("total holes: {}".format(holes))
            print("total bumps: {}".format(bumps))
            print("game status: {}".format(game_status))


    # goes through all possible combinations of hard drops
    def get_move(self):
        # fetch the current piece
        current_piece = pieces.get_piece()

        # drop each piece and add to score list
        scores = []
        pass


    def place_piece(self, piece, x):

        piece = [
        ['#', '#', '#'],
        ['#', '.', '.']
        ]
        piece.reverse()

        board = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['#', '#', '#', '.', '.', '.', '.', '.', '.', '.']
        ]
        
        piece_length = len(piece[0])

        for row_index, row in enumerate(board):
            is_clear = True
            for check_spot in range(piece_length):
                if row[x+check_spot] == '#':
                    is_clear = False
            if is_clear: 
                continue
            else:
                can_drop = True
                # can NOT drop down one more
                for drop_row in piece:
                    for drop_spot in range(len(drop_row)):
                        if board[row_index][x+drop_spot] == '#' and drop_row[drop_spot] == '#':
                            can_drop = False
                if not can_drop:
                    # transfer piece to board
                    for piece_row_index, piece_row in enumerate(piece):
                        for piece_spot_index, piece_spot in enumerate(piece_row):
                            if board[row_index-piece_row_index][x+piece_spot_index] == '.':
                                board[row_index-piece_row_index][x+piece_spot_index] = piece_spot
                    break

        for row in board:
            print(row)

