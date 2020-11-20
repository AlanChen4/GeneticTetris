import argparse
import os
import subprocess


def start_fceux(lua_test=False):
    if lua_test:
        script_path = os.path.join('test.lua')
    else:
        script_path = os.path.join('main.lua')

    save_path = 'save_states/level_0.fcs'

    start_cmd = 'fceux -lua ' + script_path + ' -loadstate ' + save_path + ' game_roms/Tetris.nes'
    subprocess.run(start_cmd, shell = True)


if __name__ == '__main__':
    description = "This is a genetic algorithm for Tetris 1989 NES"

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--tl', '-test_lua', help='runs test.lua')

    args = parser.parse_args()

    if args.tl:
        test = True
    else:
        test = False

    start_fceux(test)
