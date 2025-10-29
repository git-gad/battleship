def init_game(name1, name2) -> dict:
    player1 = name1
    player2 = name2
    map1 = [['O' for _ in range(10)] for _ in range(10)]
    map2 = [['O' for _ in range(10)] for _ in range(10)]
    display_map1 = [['O' for _ in range(10)] for _ in range(10)]
    display_map2 = [['O' for _ in range(10)] for _ in range(10)]
    state = {'player1':{'name1': name1, 'display1': display_map1},
             'player2': {'name2': name2, 'display2': display_map2},
             'map1': map1, 'map2': map2}
              
    return state 

def dispose_ships(state) -> None:
    pos_4deck = [[0, 0],[0, 1],[0, 2],[0, 3]]
    pos_3deck = [[1, 0], [1, 1], [1, 2]]     
    pos_2deck = [[2, 0], [2, 1]]             
    pos_1deck = [[3, 0]]                         
    pos_list = [pos_1deck, pos_2deck, pos_3deck, pos_4deck]
    for pos in pos_list:
        for row, column in pos:
            state['map1'][row][column] = "V"
    pos_4deck = [[9, 0],[9, 1],[9, 2],[9, 3]]
    pos_3deck = [[8, 0], [8, 1], [8, 2]]     
    pos_2deck = [[7, 0], [7, 1]]             
    pos_1deck = [[6, 0]]                         
    pos_list = [pos_1deck, pos_2deck, pos_3deck, pos_4deck]
    for pos in pos_list:
        for row, column in pos:
            state['map2'][row][column] = "V"
    
def shot(state: dict) -> None:
    shot_pos1 = [0, 2]
    shot_pos2 = [1, 3]
    shot_pos3 = [2, 4]
    shot_list = [shot_pos1, shot_pos2, shot_pos3]
    for row, column in shot_list:
        if state['map2'][row][column] == 'V':
            state['player1']['display1'][row][column] = 'V'
        else:
            state['player1']['display1'][row][column] = 'X'
    #проверить если по этим координатам есть V или O и обновить дисплей на Х если не было корабля V если был 
state = init_game('q', 'w')
   
dispose_ships(state)

shot(state)

for row in state['map2']:
    print(row)
    
print()
    
for row in state['player1']['display1']:
    print(row)
    
    
    