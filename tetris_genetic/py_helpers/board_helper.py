''''helper methods that return different characteristics of the board'''

def get_height(board):
    ''' returns the total height of the board'''
    aggregate_height = 0
    for row in range(22):
        for col in range(10):
            if board[row][col] == '#':
                aggregate_height+=1
    return aggregate_height


def get_lines_cleared(board):
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


def get_holes(board):
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


def get_bumps(board):
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

