import os
import subprocess


def start_fceux():
    script_path = os.path.join('main.lua')

    save_path = 'save_states/level_19.fcs'

    start_cmd = 'fceux -lua ' + script_path + ' -loadstate ' + save_path + ' game_roms/Tetris.nes'
    subprocess.run(start_cmd, shell = True)


if __name__ == '__main__':
    start_fceux()
