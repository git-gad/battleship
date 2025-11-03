from utils.input_output import get_coordinates
from utils.input_output import print_map
from time import sleep

def init_game(name1, name2) -> dict:
    player1 = name1
    player2 = name2
    map1 = [['🌊' for _ in range(10)] for _ in range(10)]
    map2 = [['🌊' for _ in range(10)] for _ in range(10)]
    display_map1 = [['🌊' for _ in range(10)] for _ in range(10)]
    display_map2 = [['🌊' for _ in range(10)] for _ in range(10)]
    state = {'name1': name1, 'display1': display_map1, 'ships1': [],
             'name2': name2, 'display2': display_map2, 'ships2': [],
             'map1': map1, 'map2': map2}
    return state   

def create_ship(amount_of_decks) -> list:
    ship = []
    horizontal = False
    vertical = False
    while len(ship) != amount_of_decks:  
        new_coordinates = get_coordinates()    
        if not ship:
            ship.append(new_coordinates)
        elif new_coordinates in ship:
            print('already taken')
            continue
        else:
            if horizontal:
                for row, column in ship[:]:
                    if row != new_coordinates[0]:
                        print('not valid (horizontal)')
                        break
                    elif column + 1 == new_coordinates[1] or column - 1 == new_coordinates[1]:
                        ship.append(new_coordinates)
                        break
                else:
                    print('not valid (not close)')
            elif vertical:
                for row, column in ship[:]:
                    if column != new_coordinates[1]:
                        print('not valid (vertical)')
                        break
                    elif row + 1 == new_coordinates[0] or row - 1 == new_coordinates[0]:
                        ship.append(new_coordinates)
                        break
            else:
                for row, column in ship[:]:
                    if row == new_coordinates[0]:
                        if column + 1 == new_coordinates[1] or column - 1 == new_coordinates[1]:
                            horizontal = True
                            ship.append(new_coordinates)
                    elif column == new_coordinates[1]:
                        if row + 1 == new_coordinates[0] or row - 1 == new_coordinates[0]:
                            vertical = True
                            ship.append(new_coordinates)
                else:
                    print('not valid (not close)')
        print(f'current ship {ship}')
    return ship

def create_surrounding(ship) -> set:
    surr = set()
    for row, col in ship: 
        surr.add((row, col))
        surr.add((row, col+1))
        surr.add((row, col-1))
        surr.add((row+1, col))
        surr.add((row+1, col-1))
        surr.add((row+1, col+1))
        surr.add((row-1, col))
        surr.add((row-1, col-1))
        surr.add((row-1, col+1))
    for coor in surr.copy():
        if coor[0] < 0 or coor[0] > 9 or coor[1] < 0 or coor[1] > 9:
            surr.remove(coor)
    return surr
                  
def dispose_ships(map: list, ships: list):
    list_of_decks = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    i = 0
    while i < 10:
        print_map(map)
        ship = create_ship(list_of_decks[i])
        if not ships:
            ships.append(ship)
            for row, col in ship:
                map[row][col] = '🛥️'
            i += 1
        else:
            surr = create_surrounding(ship)
            for row, col in surr:
                if map[row][col] == '🛥️':
                    print('this place is taken')
                    break
            else:
                ships.append(ship)
                for row, col in ship:
                    map[row][col] = '🛥️'
                i += 1

def shot(name: str, display: list, enemy_map: list, enemy_ships: list):
    got_shot = True
    while got_shot:
        print_map(display)
        print(f'{name} your shot')
        coor = get_coordinates()
        row, col = coor
        if enemy_map[row][col] == '🛥️':
            print('bulls eye')
            sleep(2)
        enemy_map[row][col] = display[row][col] = '☠️'
        for ship in enemy_ships[:]:
            if not ship:
                enemy_ships.remove(ship)
            if coor in ship[:]:
                ship.remove(coor)
        if not enemy_ships:
            break
        elif enemy_map[row][col] == '🌊':
            enemy_map[row][col] = display[row][col] = '❌'
            print('missed')
            sleep(2)
            got_shot = False
        elif enemy_map[row][col] == '☠️':
            print('already shot there')
            sleep(2)