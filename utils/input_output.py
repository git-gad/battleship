from os import system

def valid_input(coordinates: list):
    if len(coordinates) != 2:
        return False
    for dig in coordinates:
        if type(dig) != int or 0 > dig or dig > 9:
            return False
    return True  

def get_coordinates():
    new_coordinates = input('input coordinates in format int int\n')
    new_coordinates = new_coordinates.split()
    new_coordinates = list(map(int, new_coordinates))
    while not valid_input(new_coordinates):
        new_coordinates = input('not valid, please conform to the format\n')
        new_coordinates = new_coordinates.split()
        new_coordinates = list(map(int, new_coordinates))
    return new_coordinates

def print_map(map):
    system('cls')
    print('   0  1  2  3  4  5  6  7  8  9')
    col = 0
    for row in map:
        row = str(row)
        clean_row = row.replace('[', '').replace(']', '').replace("'", '').replace(',', '')
        print(col, clean_row)
        col += 1