from aocd import data
import copy

example1 = """0123
1234
8765
9876"""

example2 = """...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9"""

example3 = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""

example4 = """10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01"""

example5 = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

example6 = """.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9...."""

example7 = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""

example8 = """012345
123456
234567
345678
4.6789
56789."""

def pretty_print(map: list[str]):
    for line in map:
        for v in line:
            if v == -1:
                print(f'. ', end="")
            else:
                print(f'{v} ', end="")
        print()
    

def parse_map(input: str) -> list[list[int]]:
    result = []
    input_split = input.split("\n")
    for line in input_split:
        row = []
        for c in line:
            value = None
            if c == ".":
                value = -1
            else:
                value = int(c)
            row.append(value)
        result.append(row)
    return result

def find_trailheads(topology: list[list[int]]) -> list[tuple[int, int]]:
    result = []
    for i in range(0, len(topology)):
        for j in range(0, len(topology[i])):
            value = topology[i][j]
            if value == 0:
                result.append( (i, j) )
    return result

def is_legal_move(topology: list[list[int]], y_to: int, x_to: int, current_height: int) -> bool:
    if y_to < 0 or y_to > len(topology)-1:
        return False
    if x_to < 0 or x_to > len(topology[0])-1:
        return False
    to_height = topology[y_to][x_to]
    return current_height + 1 == to_height
    

def get_legal_moves(topology: list[list[int]], y_from: int, x_from: int) -> list[tuple[int, int]]:
    moves = []
    current_height = topology[y_from][x_from]
    if is_legal_move(topology, y_from + 1, x_from, current_height):
        moves.append( (y_from + 1, x_from ))
    if is_legal_move(topology, y_from - 1, x_from, current_height):
        moves.append( (y_from - 1, x_from ))
    if is_legal_move(topology, y_from, x_from + 1, current_height):
        moves.append( (y_from, x_from + 1 ))
    if is_legal_move(topology, y_from, x_from - 1, current_height):
        moves.append( (y_from, x_from - 1 ))
    return moves

def solve_trails_from_position(topology: list[list[int]], y_from: int, x_from: int, current_moves: list[tuple[int, int]]) -> list[list[tuple[int, int]]]:
    current_moves_copy = copy.deepcopy(current_moves)
    current_moves_copy.append((y_from, x_from))

    current_height = topology[y_from][x_from]
    result: list[list[tuple[int, int]]] = []
    if current_height == 9:
        result.append(current_moves_copy)
        return result
    for move in get_legal_moves(topology, y_from, x_from):
        moves = solve_trails_from_position(topology, move[0], move[1], current_moves_copy)
        if len(moves) > 0:
            for m in moves:
                result.append(m)
    return result

def remove_duplicates_based_on_last_tuple(outer_list: list[list[tuple[int, int]]]) -> list[list[tuple[int, int]]]:
    seen_last_tuples = {}
    unique_outer_list = []

    for inner_list in outer_list:
        if inner_list:
            last_tuple = inner_list[-1]
            if last_tuple not in seen_last_tuples:
                unique_outer_list.append(inner_list)
                seen_last_tuples[last_tuple] = True

    return unique_outer_list

def solve_trails_from_trailheads(topology: list[list[int]], trailheads: list[tuple[int, int]]) -> list[list[tuple[int, int]]]:
    trails = []
    resulting_sum = 0

    for trailhead in trailheads:
        trailhead_trails = solve_trails_from_position(topology, trailhead[0], trailhead[1], [])
        trails.extend(trailhead_trails)
        unique_trail_endpoints = remove_duplicates_based_on_last_tuple(trailhead_trails)
        resulting_sum = resulting_sum + len(unique_trail_endpoints)

    print("solve (a): " + str(resulting_sum))
    return trails
        
def solve_both(input: str):
    topology: list[list[int]] = parse_map(input)
    trailsheads: list[tuple[int, int]] = find_trailheads(topology)

    trails = solve_trails_from_trailheads(topology, trailsheads)
    print("Solve (b): " + str(len(trails)))

solve_both(data)