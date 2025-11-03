from input_output import *

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

def create_ship(amount_of_decks):
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

def create_surrounding(ship):
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
                  
def dispose_ships(state: dict):
    list_of_decks = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    i = 0
    while i < 10:
        ship = create_ship(list_of_decks[i])
        if not state['ships1']:
            state['ships1'].append(ship)
            for row, col in ship:
                state['map1'][row][col] = '🛥️'
            i += 1
        else:
            surr = create_surrounding(ship)
            for row, col in surr:
                if state['map1'][row][col] == '🛥️':
                    print('this place is taken')
                    break
            else:
                state['ships1'].append(ship)
                for row, col in ship:
                    state['map1'][row][col] = '🛥️'
                i += 1
    return state['map1']

# def shot(state: dict):
#     coor = get_coordinates()
#     for row, col in coor:
#         if state
        

state = init_game('gad', 'dag')

print(dispose_ships(state))
# print(create_ship(4))
for row in state['map1']:
    print(row)










# def create_ship(amount_of_decks):
#     ship = []
#     count = 0
#     while count != amount_of_decks:    
#         new_coordinates = input('input coordinates of deck in format int int\n')
#         new_coordinates = new_coordinates.split()
#         new_coordinates = list(map(int, new_coordinates))
#         while not valid_input(new_coordinates):
#             new_coordinates = input('not valid, please conform to the format\n')
#             new_coordinates = new_coordinates.split()
#             new_coordinates = list(map(int, new_coordinates))
#         if not ship:
#             ship.append(new_coordinates)
#             count += 1
#         else:
#             flag = False   
#             for coordinates in ship[:]:
#                 if sum(coordinates) == sum(new_coordinates):
#                     print('these coordinates are already taken or your ship is not straight')
#                     flag = True
#                     break
#             if not flag:
#                 for coordinates in ship[:]:
#                     if sum(coordinates) + 1 == sum(new_coordinates) or sum(coordinates) - 1 == sum(new_coordinates):
#                         ship.append(new_coordinates)
#                         count += 1
#                         break
#     return ship









# def dispose_ships(state) -> None:
#     pos_4deck = [[0, 0],[0, 1],[0, 2],[0, 3]]
#     pos_3deck = [[1, 0], [1, 1], [1, 2]]     
#     pos_2deck = [[2, 0], [2, 1]]             
#     pos_1deck = [[3, 0]]                         
#     pos_list = [pos_1deck, pos_2deck, pos_3deck, pos_4deck]
#     for pos in pos_list:
#         for row, column in pos:
#             state['map1'][row][column] = "V"
#     pos_4deck = [[9, 0],[9, 1],[9, 2],[9, 3]]
#     pos_3deck = [[8, 0], [8, 1], [8, 2]]     
#     pos_2deck = [[7, 0], [7, 1]]             
#     pos_1deck = [[6, 0]]                         
#     pos_list = [pos_1deck, pos_2deck, pos_3deck, pos_4deck]
#     for pos in pos_list:
#         for row, column in pos:
#             state['map2'][row][column] = "V"
    
# def shot(state: dict) -> None:
#     shot_pos1 = [0, 2]
#     shot_pos2 = [1, 3]
#     shot_pos3 = [2, 4]
#     shot_list = [shot_pos1, shot_pos2, shot_pos3]
#     for row, column in shot_list:
#         if state['map2'][row][column] == 'V':
#             state['player1']['display1'][row][column] = 'V'
#         else:
#             state['player1']['display1'][row][column] = 'X'
#     #проверить если по этим координатам есть V или O и обновить дисплей на Х если не было корабля V если был 
# state = init_game('q', 'w')
   
# dispose_ships(state)

# shot(state)

# for row in state['map2']:
#     print(row)
    
# print()
    
# for row in state['player1']['display1']:
#     print(row)
    
    
    