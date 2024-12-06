from aocd import data
from typing import Dict


example = """3   4
4   3
2   5
1   3
3   9
3   3"""

def splitData(input: str) -> list[list[int]]:
    first_list: list[int] = []
    second_list: list[int] = []

    data_arr = input.split('\n')
    for s in data_arr:
        parts = s.split()
        first_list.append(int(parts[0]))
        second_list.append(int(parts[1]))

    first_list.sort()
    second_list.sort()
    return [first_list, second_list]

def intCount(input: list[int]) -> Dict[int, int]:
    result_map = {}
    for i in range(0, len(input)):
        value = input[i]
        if (value in result_map):
            result_map[value] = result_map.get(value) + 1
        else:
            result_map[value] = 1
    return result_map

def solve_a(input: str):
    split_arrays: list[list[int]] = splitData(input)
    # print(split_arrays)

    arr1 = split_arrays[0]
    arr2 = split_arrays[1]

    if (len(arr1) != len(arr2)):
        print("Different lenght lists -- this shouldn't happen")
        exit()

    distance_total = 0
    for i in range(0, len(arr1)):
        left_item = arr1[i]
        right_item = arr2[i]
        distance = abs(left_item-right_item)
        distance_total += distance
    print("Total distance: " + str(distance_total))


def solve_b(input: str):
    split_arrays: list[list[int]] = splitData(input)

    arr1 = split_arrays[0]
    arr2 = split_arrays[1]

    left_count_map = intCount(arr1)
    right_count_map = intCount(arr2)


    similarity_score = 0    
    for key in left_count_map:
        right_count = 0
        left_count = left_count_map[key]

        if key in right_count_map:
            right_count = right_count_map.get(key)

        similarity_score += key * right_count * left_count
    
    print("Similarity score: " + str(similarity_score))


solve_a(data)
solve_b(data)