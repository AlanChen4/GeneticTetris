i_piece = [['#', '#', '#', '#']]

j_piece = [['#', '.', '.'],
           ['#', '#', '#']]

l_piece = [['.', '.', '#'],
           ['#', '#', '#']]

s_piece = [['.', '#', '#'],
           ['#', '#', '.']]

z_piece = [['#', '#', '.'],
           ['.', '#', '#']]

t_piece = [['.', '#', '.'],
           ['#', '#', '#']]

o_piece = [['#', '#'],
           ['#', '#']]


def rotate_piece(piece):
    # rotated version
    rotated = zip(*piece[::-1])
    rotated = [list(spot) for spot in rotated]
    return rotated
    

def get_piece():
    current_piece_id = open('py_helpers/game_state/current_next_piece.txt')
    print(current_piece_id.read())
