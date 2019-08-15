import numpy as np

i_piece = [['#', '#', '#', '#']]

j_piece = [['#', '.', '.'],
           ['#', '#', '#']]

l_piece = [['#', '#', '#'],
           ['#', '.', '.']]

s_piece = [['.', '#', '#'],
           ['#', '#', '.']]

z_piece = [['#', '#', '.'],
           ['.', '#', '#']]

t_piece = [['.', '#', '.'],
           ['#', '#', '#']]

o_piece = [['#', '#'],
           ['#', '#']]


def rotate_piece(piece, rotation_count):
    rotated_piece = np.array(piece)
    rotated_piece = np.rot90(rotated_piece, rotation_count)
    return rotated_piece


def get_piece(console):
    current_piece_id = open('py_helpers/game_state/current_next_piece.txt')
    try:
        current_piece_id = int(current_piece_id.read().split(' ')[1])
        if current_piece_id == 2:
            return_piece = t_piece
        if current_piece_id == 14:
            return_piece = l_piece
        if current_piece_id == 8:
            return_piece = z_piece
        if current_piece_id == 10:
            return_piece = o_piece
        if current_piece_id == 7:
            return_piece = j_piece
        if current_piece_id == 18:
            return_piece = i_piece
        if current_piece_id == 11:
            return_piece = s_piece

        if console:
            print('')
            for row in return_piece:
                print(row)
            print('')

        return return_piece

    except IndexError:
        pass
    except ValueError:
        pass
