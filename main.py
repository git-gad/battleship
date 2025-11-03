from utils.game_logic import *
from utils.input_output import print_map

if __name__ == '__main__':
    name1 = input('player1 name: ')
    name2 = input('player2 name: ')
    state = init_game(name1, name2)
    dispose_ships(state['map1'], state['ships1'])
    dispose_ships(state['map2'], state['ships2'])
    while True:
        print_map(state['display1'])
        shot(state['name1'], state['display1'], state['map2'], state['ships2'])
        if not state['ships2']:
            print(f'{state["name1"]} won')
            break
        print_map(state['display1'])
        shot(state['name2'], state['display2'], state['map1'], state['ships1'])
        if not state['ships1']:
            print(f'{state["name2"]} won')
            break