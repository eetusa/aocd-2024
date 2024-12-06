from aocd import data
from typing import Dict

example = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def get_reports(input: str) -> list[list[int]]:
    report_array = input.split('\n')
    result: list[list[int]] = []

    for report in report_array:
        string_list = report.split(" ")
        result.append([int(num) for num in string_list if num])

    return result

def is_level_gradient_safe(left: int, right: int, increasing: bool) -> bool:
    if (left == right):
        return False
    
    if (abs(left-right) > 3):
        return False

    if (left > right):
        if (increasing == True):
            return False
    else:
        if (increasing == False):
            return False
    return True

def is_report_safe(report: list[int]) -> bool:
    increasing = None

    if (report[0] > report[1]):
        increasing = False
    elif (report[1] > report[0]):
        increasing = True
    else:
        return False

    for i in range(0, len(report) - 1):
        left: int = report[i]
        right: int = report[i + 1]

        if (is_level_gradient_safe(left, right, increasing) == False):
            return False
    return True

def get_safe_count(reports: list[list[int]]) -> int:
    safe_count: int = 0
    for report in reports:
        if is_report_safe(report):
            safe_count = safe_count + 1
    return safe_count


def is_report_safe_with_dampener(report: list[int]) -> bool:
    if (is_report_safe(report) == True):
        return True

    # Brute force through dampened reports
    for i in range(len(report)):
        dampened_report = report[:i] + report[i+1:]
        safe = is_report_safe(dampened_report)
        if (safe == True):
            return True
    return False

def get_safe_count_with_dampener(reports: list[list[int]]) -> int:
    safe_count: int = 0
    for report in reports:
        if is_report_safe_with_dampener(report):
            safe_count = safe_count + 1
    return safe_count

def solve_a(input: str):
    reports: list[list[int]] = get_reports(input)
    safe_count: int = get_safe_count(reports)
    print("Safe count (a): " + str(safe_count))

def solve_b(input: str):
    reports: list[list[int]] = get_reports(input)
    safe_count: int = get_safe_count_with_dampener(reports)
    print("Safe count (b): " + str(safe_count))

solve_a(data)
solve_b(data)
