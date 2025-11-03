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