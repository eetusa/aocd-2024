from aocd import data
import itertools
from typing import Dict
from typing import Set, Tuple

example = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

example0 = """..........
..........
.32.......
....a.....
..2.......
.....a....
..........
..........
........3.
.........."""

example2 = """T.........
...T......
.T........
..........
..........
..........
..........
..........
..........
.........."""

def parse_map(input: str):
    return input.split("\n")

def pretty_print(map: list[str]):
    for line in map:
        print(line)

def pretty_print_with_antinodes(map: list[str], antinodes: Set[Tuple[int, int]]):
    for i in range(0, len(map)):
        line = ""
        for j in range(0, len(map[i])):
            if (i, j) in antinodes:
                line = line + "#"
            else:
                line = line + map[i][j]
        print(line)

def get_antennas(map: list[str]) -> Dict[str, list[Tuple[int, int]]]:
    antennas: dict[str, list[Tuple[int, int]]] = {}

    for n in range(0, len(map)):
        for m in range(0, len(map[0])):
            value = map[n][m]
            if value == ".":
                continue
            if value in antennas:
                antennas[value].append( (n, m) )
            else:
                antennas[value] = [ (n, m) ]
    return antennas

def is_inside_map(x, y, width, height):
    return 0 <= x < width and 0 <= y < height

def calculate_antinodes(a: Tuple[int, int], b: Tuple[int, int], map_width: int, map_height: int) -> list[Tuple[int, int]]:
    result = []
    x1, y1 = a
    x2, y2 = b

    dx = x2 - x1
    dy = y2 - y1

    first = ( x1 - dx, y1 - dy )
    second = ( x2 + dx, y2 + dy )

    if is_inside_map(first[0], first[1], map_width, map_height):
        result.append(first)
    if is_inside_map(second[0], second[1], map_width, map_height):
        result.append(second)

    return result

def calculate_antinodes_in_lines(a: Tuple[int, int], b: Tuple[int, int], map_width: int, map_height: int) -> list[Tuple[int, int]]:
    result = []

    x1, y1 = a
    x2, y2 = b

    dx = x2 - x1
    dy = y2 - y1

    running_x = x1
    running_y = y1

    while(True):
        target = ( running_x + dx, running_y + dy )
        if not is_inside_map(target[0], target[1], map_width, map_height):
            break
        result.append(target)
        running_x = target[0]
        running_y = target[1]

    running_x = x2
    running_y = y2

    while(True):
        target = ( running_x - dx, running_y - dy )
        if not is_inside_map(target[0], target[1], map_width, map_height):
            break
        result.append(target)
        running_x = target[0]
        running_y = target[1]

    return result

def get_antinodes(antennas: Dict[str, list[Tuple[int, int]]], map_width: int, map_height: int, isA: bool) -> Set[Tuple[int, int]]:
    antinodes: Set[Tuple[int, int]] = set()

    for key in antennas:
        antennas_sublist = antennas[key]
        for i in range(0, len(antennas_sublist) - 1):
            a: Tuple[int, int] = antennas_sublist[i]
            for j in range(i + 1, len(antennas_sublist)):
                b: Tuple[int, int] = antennas_sublist[j]
                if isA:
                    calculated_antinodes = calculate_antinodes(a, b, map_width, map_height)
                else:
                    calculated_antinodes = calculate_antinodes_in_lines(a, b, map_width, map_height)
                for antinode in calculated_antinodes:
                    if not antinode in antinodes:
                        antinodes.add(antinode)

    return antinodes

def solve_a(input: str):
    map = parse_map(input)
    map_width = len(map[0])
    map_height = len(map)

    #pretty_print(map)

    antennas: Dict[str, list[Tuple[int, int]]] = get_antennas(map)

    antinodes = get_antinodes(antennas, map_width, map_height, True)
    #pretty_print_with_antinodes(map, antinodes)
    print("solve (a): " + str(len(antinodes)))


def solve_b(input: str):
    map = parse_map(input)
    map_width = len(map[0])
    map_height = len(map)

    #pretty_print(map)
    antennas: Dict[str, list[Tuple[int, int]]] = get_antennas(map)

    antinodes = get_antinodes(antennas, map_width, map_height, False)
    #pretty_print_with_antinodes(map, antinodes)
    print("solve (b): " + str(len(antinodes)))

solve_a(data)
solve_b(data)