import cv2
import json
import time

class Heuristics:


    def convert_image(self):
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
        if debug:
            # delay for debugging purposes
            time.sleep(1)

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
            print("\n"*50)
            for row in self.board:
                print(row)


    def get_height(self):
        # loop through each row for filled spots
        aggregate_height = 0
        for row in range(22):
            for col in range(10):
                if self.board[row][col] == '#':
                    aggregate_height+=1
        return aggregate_height


    def get_lines_cleared(self):
        return None


    def get_holes(self):
        return None


    def get_bumps(self):
        return None


    # TODO check to make sure that this works
    def update_info(self):

        print("aggregate height: {}".format(self.get_height()))
        print("lines cleared: {}".format(self.get_lines_cleared()))
        print("total holes: {}".format(self.get_holes()))
        print("total bumps: {}".format(self.get_bumps()))


        info = {
        'height': self.get_height(),
        'lines_cleared': self.get_lines_cleared(),
        'holes': self.get_holes(),
        'bumps': self.get_bumps()
        }

        with open('game_state/game_status.json', 'w') as file:
            json.dump(info, file)
        
