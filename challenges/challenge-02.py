import util
from functools import reduce
from operator import mul

input = util.get_input(2)

ParsedGame = list[tuple[int, dict[str, int]]]

def parse_game(game: str) -> ParsedGame:
    id = int(game.split(": ")[0].split(" ")[1])
    grabs = game.split(": ")[1].split("; ")
    parsed_grabs = []

    for grab in grabs:
        parsed_grab = {}

        for entry in grab.split(", "):
            parts = entry.split(" ")
            colour = parts[1]
            quantity = int(parts[0])

            parsed_grab[colour] = quantity
        
        parsed_grabs.append(parsed_grab)
    
    return (id, parsed_grabs)

def get_minimums(game: ParsedGame):
    totals = {}

    for grab in game[1]:
        for colour, quantity in grab.items():
            if colour in totals and quantity > totals[colour]:
                totals[colour] = quantity
            elif colour not in totals:
                totals[colour] = quantity
    
    return totals

# Part 1
games = [parse_game(game) for game in input]
minimums = [(game[0], get_minimums(game)) for game in games]

sum = 0

for game in minimums:
    colours = game[1]
    valid_red = "red" in colours and colours["red"] <= 12
    valid_green = "green" in colours and colours["green"] <= 13
    valid_blue = "blue" in colours and colours["blue"] <= 14

    if valid_red and valid_green and valid_blue:
        sum += game[0]

print(f"Part 1: {sum}")

# Part 2
sum = 0

for game in minimums:
    colours = game[1]
    operands = [colours[color] for color in ["red", "green", "blue"] if color in colours]

    if len(operands) > 0:
        sum += reduce(mul, operands, 1)

print(f"Part 2: {sum}")