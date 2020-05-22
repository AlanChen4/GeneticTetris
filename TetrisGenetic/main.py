import os
import subprocess

def start_fceux():
        '''Starts fceux with the lua script'''
        script_path = os.path.join('tetris-AI.lua')
        save_path = 'save_states/level_0.fcs'

        start_cmd = 'fceux -lua ' + script_path + ' -loadstate ' + save_path + ' game_roms/Tetris.nes'
        subprocess.run(start_cmd, shell = True)

if __name__ == '__main__':
    start_fceux()
