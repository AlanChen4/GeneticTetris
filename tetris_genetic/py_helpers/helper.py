import cv2
import json
import time

from copy import deepcopy

from py_helpers import pieces
from py_helpers import board_helper

class Heuristics:
	''' Gathers the information needed for the lua-based AI'''

	def __init__(self):
		while True:
			if self.update_board():
				self.get_decision()


	def update_board(self):
		'''updates self._board based on the game screen'''
		if self.get_game_status() == 2:

			self.convert_image()
			self._board = []
			converted_image = cv2.imread('game_state/converted_image.png')
			
			for row in range(22):
				for col in range(10):
					if col%10 == 0:
						self._board.append([])
					if converted_image[row][col][0] == 0:
						self._board[row].append('.')
					else:
						self._board[row].append('#')
			return True

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


	def get_board_data(self, board):
		'''returns height, lines_cleared, holes, and bumpiness'''
		aggregate_height = board_helper.get_height()
		lines_cleared = board_helper.get_lines_cleared()
		total_holes = board_helper.get_holes()
		bumpiness = board_helper.get_bumps()
		return aggregate_height, lines_cleared, total_holes, bumpiness


	def get_game_status(self):
		'''returns status of the game from RAM map'''
		try:
			game_status = int(open('game_state/fceux_status.txt', 'r').read())
		except ValueError:
			game_status = 0
		return game_status


	def get_decision(self):
		'''makes every possible hypothetical move, return best option'''
		self._hypo_scores = []
		piece = pieces.get_piece(console=False)

		# make every move possible
		for arrangement in range(4):
			r_piece = pieces.rotate_piece(piece, arrangement)
			for x_location in range(10 - len(r_piece[0])):
				self.place_piece(x_location, r_piece, arrangement)


		# sort and pick best move
		highest_score = -100000
		highest_score_index = None
		for score_index, score in enumerate(self._hypo_scores):
		    if score['score'] > highest_score:
		        highest_score = score['score']
		        highest_score_index = score_index

		best_board = self._hypo_scores[highest_score_index]['board']
		print('score:', self._hypo_scores[highest_score_index]['score'])
		print('x-value:', self._hypo_scores[highest_score_index]['x_value'])
		print('rotations:', self._hypo_scores[highest_score_index]['rotations'])
		for r in best_board:
		    print(r)


	def place_piece(self, x, piece, rotate_times):
		'''places piece in x value with given rotations'''
		self._hypo_board = deepcopy(self._board)
		piece_length = len(piece[0])

		for row_index in range(22):
			# reached bottom
			if row_index == 21:
				for row_p_index, row_piece in enumerate(piece):
					for spot_index, spot_piece in enumerate(row_piece):
						row_value = (22-len(piece))+row_p_index
						if self._hypo_board[row_value][x+spot_index] == '.':
							self._hypo_board[row_value][x+spot_index] = spot_piece 
				break
		    # piece confliction
			elif '#' in self._hypo_board[row_index+1]:
		        # determine is there are any pieces in conflict
				is_piece = False
				for piece_row_index, piece_row in enumerate(piece):
				    for spot_index, spot_value in enumerate(piece_row):
				        if spot_value == '#':
				            if self._hypo_board[row_index-((len(piece)-2)-piece_row_index)][spot_index+x] == '#':
				                is_piece = True
				if is_piece:
				    for piece_row_index, piece_row in enumerate(piece):
				        for spot_index, spot_value in enumerate(piece_row):
				            if self._hypo_board[(row_index-len(piece))+piece_row_index+1][spot_index+x] == '.':
				                self._hypo_board[(row_index-len(piece))+piece_row_index+1][spot_index+x] = spot_value
				    break

		# get weights generated from lua_file
		height_w, line_w, hole_w, bump_w = open('py_helpers/game_state/lua_weights.txt').read().split(' ')

		# get values determined by move made
		height_v = int(board_helper.get_height(self._hypo_board))
		line_v = int(board_helper.get_lines_cleared(self._hypo_board))
		hole_v = int(board_helper.get_holes(self._hypo_board))
		bump_v = int(board_helper.get_bumps(self._hypo_board))

		# place score value along with x_value and rotations
		score = (float(height_w)*height_v) + (float(line_w)*line_v) + (float(hole_w)*hole_v) + (float(bump_w)*bump_v)
		score_info = {'score': score , 'x_value': x, 'rotations': rotate_times, 'board': self._hypo_board}
		self._hypo_scores.append(score_info)