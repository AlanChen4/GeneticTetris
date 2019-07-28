import cv2
import json
import time


def convert_image():
    try:
        status_image = cv2.imread("game_state/status.png")
        cropped_image = status_image[40:200, 95:175]
        colored_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
        final_image = cv2.resize(colored_image, (10, 22))

        cv2.imwrite('game_state/converted_image.png', final_image)
    except TypeError:
        # TypeError is raised when status.png has not been created
        pass


def update_board(debug):
    if debug:
        # delay for debugging purposes
        time.sleep(1)

    # converts the image into an array
    board = []
    converted_image = cv2.imread('game_state/converted_image.png')
    for row_index, row in enumerate(converted_image):
        for spot_index, spot in enumerate(row):
            if spot_index % 10 == 0:
                board.append([])
                if spot[0] != 0:
                    board[row_index].append('#')
            elif spot[0] != 0:
                board[row_index].append('#')
            else:
                board[row_index].append('.')
    
    if debug:
        # clears command prompt and prints array in tetris format
        print("\n"*50)
        for row in board:
            print(row)


def get_height():
    pass


def get_lines_cleared():
    pass


def get_holes():
    pass


def get_bumps():
    pass

# check to make sure that this works
def update_info():
    info = {
    'height': get_height(),
    'lines_cleared': get_lines_cleared(),
    'holes': get_holes(),
    'bumps': get_bumps()
    }

    with open('game_status.json', 'w') as file:
        json.dump(info, file)
    
