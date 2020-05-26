import argparse
import os
import subprocess


def start_fceux(lua_test):
    '''Starts fceux with the appropriate lua script'''
    if lua_test:
        script_path = os.path.join('test.lua')
    else:
        script_path = os.path.join('main.lua')

    save_path = 'save_states/level_0.fcs'

    start_cmd = 'fceux -lua ' + script_path + ' -loadstate ' + save_path + ' game_roms/Tetris.nes'
    subprocess.run(start_cmd, shell = True)


if __name__ == '__main__':
    # program description
    description = "This is a genetic algorithm for Tetris 1989 NES"

    # initiate parser
    parser = argparse.ArgumentParser(description = description)

    # add arguments to parser
    parser.add_argument('--tl', '-test_lua', help = 'runs test.lua')

    args = parser.parse_args()

    if args.tl:
        test = True
    else:
        test = False

    start_fceux(test)

