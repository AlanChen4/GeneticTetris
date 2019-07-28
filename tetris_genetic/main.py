import subprocess
import threading

from py_helpers import helper

class tetris_AI:

    def __init__(self):
        self.jobs = []


    def start_script(self):
        '''Starts fceux with the lua script'''
        script_path = 'tetris_AI.lua'
        save_path = 'save_states/level_0.fcs'
        subprocess.run('fceux -lua ' + script_path + ' -loadstate ' + save_path + ' game_roms/Tetris.nes')


    def start_helper(self):
        '''Starts python helper script'''

        while True:
            helper.convert_image()
            helper.update_board(debug=True)


    def start_all(self):
        self.jobs.append(threading.Thread(target=self.start_script))
        self.jobs.append(threading.Thread(target=self.start_helper))

        for job in self.jobs:
            job.start()


AI = tetris_AI()
AI.start_all()
