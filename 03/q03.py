from aocd import data
from typing import Dict
import re

EXAMPLE1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
EXAMPLE2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

MULTIPLICATION_PATTERN = r'mul\(\d+,\d+\)'
DO_PATTERN = r"do\(\)"
DONT_PATTERN = r"don't\(\)"
COMBINED_PATTERN = f'({MULTIPLICATION_PATTERN})|({DO_PATTERN})|({DONT_PATTERN})'

def extract_valid_patterns_with_indexes(input, pattern):
    matches = re.finditer(pattern, input)
    results = [(match.start(), match.group()) for match in matches]
    return results

def extract_integers(instruction: str) -> list[int]:
    trimmed_instruction = instruction[4:]
    trimmed_instruction = trimmed_instruction[:-1]
    trimmed_instruction_split = trimmed_instruction.split(",")
    return [int(num) for num in trimmed_instruction_split if num]

def get_result(instructions: list[tuple[int, str]], ignore_permissions: bool):
    sum = 0
    do_calculate = True

    for index, instruction in instructions:
        if instruction == "do()":
            do_calculate = True
            continue
        if instruction == "don't()":
            do_calculate = False
            continue

        if (ignore_permissions == False and do_calculate == False):
            continue

        multiplication_parameters = extract_integers(instruction)
        sum = sum + multiplication_parameters[0] * multiplication_parameters[1]
    
    return sum

def solve_a(input):
    all_matches = extract_valid_patterns_with_indexes(input, COMBINED_PATTERN)
    result = get_result(all_matches, True)
    print("solve (a): " + str(result))

def solve_b(input):
    all_matches = extract_valid_patterns_with_indexes(input, COMBINED_PATTERN)
    result = get_result(all_matches, False)
    print("solve (b): " + str(result))


solve_a(data)
solve_b(data)
