import numpy as np

class board_simulation:
	'''creates a board environment to simulate within'''

	def __init__(self):
		self.board = []
		self.clear_board()

	def clear_board(self):
		'''clears board or creates empty board if it is not created yet'''
		if self.board == []:
			# adds the rows
			for i in range(20):
				self.board.append(10 * ['.'])

	def show_board(self):
		'''prints board out'''
		# board is reversed so it shows actual board
		for row_index, row in enumerate(reversed(self.board)):
			print(row, 19-row_index)

	def scan_board(self):
		'''scans the board with indexs'''
		value = np.array(self.board)
		for index, value in np.ndenumerate(value):
			print(index, value)


c = board_simulation()
c.show_board()