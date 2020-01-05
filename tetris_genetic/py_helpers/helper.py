import cv2
import json
import os
import subprocess
import threading
import time

from copy import deepcopy

from py_helpers import pieces
from py_helpers import board_helper

GENERATION_COUNT = 0
INDIVIDUAL_COUNT = 1

class Heuristics:
	''' Gathers the information needed for the lua-based AI'''

	# TODO: looks like pieces are never placed in the first or last spots

	def __init__(self):
		# creates live version of fceux screen
		self.live_board = []
		for row in range(22):
			for col in range(10):
				if col % 10 == 0:
					self.live_board.append(['.'])
				else:
					self.live_board[row].append('.')

		# show basic data after starting fceux thread
		threading.Thread(target=self.start_fceux).start()
		print('Waiting for fceux to start...')
		time.sleep(2)
		self.bot_status()

		self.start_AI()


	def start_AI(self):
		is_playing = True
		print('Currently playing the game')
		while is_playing:
			game_status = self.get_game_status()
			if game_status == 10:
				is_playing = False
				print('Game is not in playable state')
				break
			else:
				is_playing = True


	def start_fceux(self):
		'''Starts fceux with the lua script'''
		script_path = os.path.join('tetris_AI.lua')
		save_path = 'save_states/level_0.fcs'

		start_cmd = 'fceux -lua ' + script_path + ' -loadstate ' + save_path + ' game_roms/Tetris.nes'
		subprocess.run(start_cmd, shell = True)


	def bot_status(self):
		''' shows general information'''
		print('|--------------------|')

		# TODO: fix generation and individual count later
		print('GENERATION: ', GENERATION_COUNT, 'INDIVIDUAL: ', INDIVIDUAL_COUNT)
		print(self.get_lua_weights())

		aggregate_height = board_helper.get_height(self.live_board)
		lines_cleared = board_helper.get_lines_cleared(self.live_board)
		total_holes = board_helper.get_holes(self.live_board)
		bumpiness = board_helper.get_bumps(self.live_board)
		
		print('aggregate_height: ', aggregate_height)
		print('lines_cleared: ', lines_cleared)
		print('total_holes: ', total_holes)
		print('bumpiness: ', bumpiness)
		print('|--------------------|')


	def get_lua_weights(self):
		'''returns weights generated from lua_file'''
		height_w, line_w, hole_w, bump_w = open('py_helpers/game_state/lua_weights.txt').read()[1:].split(' ')
		return height_w, line_w, hole_w, bump_w


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
		self.get_board_data(self._board)


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
		height_w, line_w, hole_w, bump_w = self.get_lua_weights()

		# get values determined by move made
		height_v = int(board_helper.get_height(self._hypo_board))
		line_v = int(board_helper.get_lines_cleared(self._hypo_board))
		hole_v = int(board_helper.get_holes(self._hypo_board))
		bump_v = int(board_helper.get_bumps(self._hypo_board))

		# place score value along with x_value and rotations
		score = (float(height_w)*height_v) + (float(line_w)*line_v) + (float(hole_w)*hole_v) + (float(bump_w)*bump_v)
		score_info = {'score': score , 'x_value': x, 'rotations': rotate_times, 'board': self._hypo_board}
		self._hypo_scores.append(score_info)