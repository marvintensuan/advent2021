with open('inputs/day2.txt') as file:
    txt = file.read()
    data = tuple(map(str,txt.split(sep='\n')))

position = [0, 0, 0] #horizontal, depth, aim

def move(unit: list, command: str):
    direction, units = command.split(" ")
    match direction:
        case 'forward':
            unit[0] += int(units)
            unit[1] += (unit[2] * int(units))
        case 'up':
            unit[2] -= int(units)
        case 'down':
            unit[2] += int(units)

for cmd in data:
    move(position, cmd)

print(position, position[0] * position[1])