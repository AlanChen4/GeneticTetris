''''helper methods that return different functions inside the fceux environment'''

def send_command(command):
	'''lets the fceux thread know what to do while the python processes are running'''
	# current commands: wait, restart, down
	with open('game_state/AI_decision.txt', 'w') as f:
		f.write(command)
		f.close()

