from __future__ import annotations
from aocd import data
from typing import Dict

example0 = "0 1 10 99 999"
example =  "125 17"

def parse_input(input: str) -> Dict[int, int]:
    result: Dict[int, int] = {}
    for n in input.split(" "): 
        n = int(n)
        if n in result:
            result[n] = result[n] + 1
        else:
            result[n] = 1
    return result

def add_to_map(stone_map: Dict[int, int], value, value_count):
    if value in stone_map:
        stone_map[value] = stone_map[value] + value_count
    else:
        stone_map[value] = value_count

def get_map_total(stone_map: Dict[int, int]):
    sum = 0
    for key in stone_map:
        sum = sum + stone_map[key]
    return sum

def blink(initial_stone_map: Dict[int, int], blink_count: int):
    stone_map = initial_stone_map
    print(stone_map)

    for i in range(0, blink_count):
        new_stones: Dict[int, int] = {}
        
        for value in stone_map:
            value_count = stone_map[value]

            if value == 0:
                add_to_map(new_stones, 1, value_count)
            elif len(str(value)) % 2 == 0:
                value_str = str(value)
                mid = len(value_str) // 2
                first_half = int(value_str[:mid])
                second_half = int(value_str[mid:])

                add_to_map(new_stones, first_half, value_count)
                add_to_map(new_stones, second_half, value_count)
            else:
                new_value = value * 2024
                add_to_map(new_stones, new_value, value_count)

        stone_map = new_stones

    return get_map_total(stone_map)

def solve(input: str, blink_count: int, excercise: str) -> int:
    stone_map = parse_input(input)

    stone_count = blink(stone_map, blink_count)
    print(f'Solve ({excercise}): {stone_count}')

#solve("125 17", 6, "example")
solve(data, 25, "a")
solve(data, 75, "b")