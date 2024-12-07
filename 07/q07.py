from aocd import data
import itertools
from typing import Dict

example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

OPERATORS_CACHE: dict[int, list[str]] = {}

def parseEquations(input: str) -> list[tuple[int, list[int]]]:
    lines = input.split("\n")
    result: list[tuple[int, list[int]]] = []
    for line in lines:
        line_split = line.split(":")
        value = line_split[0]
        parameters_str = ((line_split[1])[1:]).split(" ")
        parameters = [int(num) for num in parameters_str if num]

        result.append( (int(value), parameters) )
    
    return result

def generate_operator_combinations(operators, length):
    if length in OPERATORS_CACHE:
        return OPERATORS_CACHE.get(length)

    combinations = list(itertools.product(operators, repeat=length))
    operator_combinations = [list(combination) for combination in combinations]
    
    OPERATORS_CACHE[length] = operator_combinations
    return operator_combinations

def multiply_first_two(equation: tuple[int, list[int]]):
    return None

def is_equation_solvable(equation: tuple[int, list[int]], operators: str) -> bool:
    value = equation[0]
    parameters = equation[1]
    operators_count = len(parameters) - 1
    all_operator_combinations: list[tuple[str]] = generate_operator_combinations(operators, operators_count)

    for operator_combination in all_operator_combinations:
        left_value = parameters[0]

        for i in range(1, len(parameters)):
            if operator_combination[i-1] == "*":
                left_value = left_value * parameters[i]
            if operator_combination[i-1] == "+":
                left_value = left_value + parameters[i]
            if operator_combination[i-1] == "||":
                left_value = int(str(left_value) + str(parameters[i]))
        if left_value == value:
            return True

    return False

def solve_a(input: str):
    OPERATORS_CACHE = {}

    equations = parseEquations(input)
    solved_values_sum = 0
    for equation in equations:
        solvable: bool = is_equation_solvable(equation, ["+", "*"])
        if solvable:
            solved_values_sum = solved_values_sum + equation[0]

    print("solve (a): " + str(solved_values_sum))

def solve_b(input: str, debug: bool):
    OPERATORS_CACHE = {}

    equations = parseEquations(input)
    solved_values_sum = 0
    process_count = 0
    for equation in equations:
        solvable: bool = is_equation_solvable(equation, ["+", "*", "||"])
        if solvable:
            solved_values_sum = solved_values_sum + equation[0]
        process_count = process_count + 1

        if (debug):
            if process_count % 10 == 0:
                print(str(process_count) + "/" + str(len(equations)))
    print("solve (b): " + str(solved_values_sum))

solve_a(data)
solve_b(data, True)