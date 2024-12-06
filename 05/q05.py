from aocd import data
from typing import Dict
from collections import defaultdict, deque

example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def get_rules(rules_input: str) -> list[tuple[str, str]]:
    rules_input_split = rules_input.split("\n")

    rules = []
    #print(rules_input)
    for rule in rules_input_split:
        rule_split = rule.split("|")
        rules.append((rule_split[0], rule_split[1]))
    return rules

def removeElementAtIndex(array: list[str], index: int) -> list[str]:
    if 0 <= index < len(array):
        del array[index]
    return array

def addElementAtIndex(array: list[str], index: int, value: str) -> list[str]:
    array.insert(index, value)
    return array

def form_initial_list(rules: list[tuple[str, str]]):
    initial_list: list[str] = []
    for rule in rules:
        before_value = rule[0]
        after_value = rule[1]
        if not before_value in initial_list:
            initial_list.append(before_value)
        if not after_value in initial_list:
            initial_list.append(after_value)

    return initial_list


def check_rules(rules: list[tuple[str, str]], page_order: list[str]):
    broken_count = 0
    for rule in rules:
            before_value = rule[0]
            after_value = rule[1]

            before_value_index = page_order.index(before_value)
            after_value_index = page_order.index(after_value)

            if (before_value_index > after_value_index):
                print("Rule broken: " + str(rule))
                print("i: " + str(before_value_index) + " | i: " + str(after_value_index))
                broken_count = broken_count + 1
    print(str(broken_count) + " rules broken")

def form_page_ordering(rules: list[tuple[str, str]]) -> list[str]:
    page_order: list[str] = form_initial_list(rules)
    iteration_counter = 0

    while(True):
        did_fix = False
        for rule in rules:
            before_value = rule[0]
            after_value = rule[1]
            
            before_value_index = page_order.index(before_value)
            after_value_index = page_order.index(after_value)

            if (before_value_index > after_value_index):
                #print("----")
                #print(page_order)
                #print(rule)
                #print("i: " + str(before_value_index) + " | i: " + str(after_value_index))
                #input()
                did_fix = True
                page_order = removeElementAtIndex(page_order, before_value_index)
                page_order = addElementAtIndex(page_order, after_value_index, before_value)
                #print(page_order)
                #print()


        iteration_counter = iteration_counter + 1
        if (did_fix == False):
            break
        if (iteration_counter > 10000):
            print("Couldn't solve page order deterministically, returning _something_")
            break
    return page_order

def is_page_update_valid(page_order: list[str], page_update: list[str]):
    update_page_indexes = []

    for value in page_update:
        update_page_indexes.append(page_order.index(value))
    
    for i in range(0, len(page_update) -1):
        if not page_update[i] in page_order:
            continue
        if not page_update[i+1] in page_order:
            continue
        left_value = page_order.index(page_update[i])
        right_value = page_order.index(page_update[i+1])

        if right_value < left_value:
            return False
    return True

def get_rule_subset_2(all_rules: list[tuple[str, str]], update: list[str]):
    rule_subset = {}

    for rule in all_rules:
        left = rule[0]
        right = rule[1]
        if (not left in update) and (not right in update):
            continue
        else:
            rule_subset.setdefault(left, []).append(right)
    return rule_subset
                    
def is_value_in_rules(rules: list[tuple[str, str]], value: str):
    for rule in rules:
        left = rule[0]
        right = rule[1]
        if (value == left) or (value == right):
            return True
    return False

def is_page_valid_with_subset(rules: dict[str, list[str]], update: list[str]):
    processed = []
    for i in range(0, len(update)):
        value = update[i]
        value_rules = rules.get(value)
        if (value_rules == None): 
            processed.append(value)
            continue

        for p in processed:
            if p in value_rules:
                return False
        processed.append(value)
    return True

def solve_a(input: str):
    input_split = input.split("\n\n")
    rules = get_rules(input_split[0])
    page_updates = input_split[1].split("\n")
    update_sum = 0

    for page_update in page_updates:
        page_update_split = page_update.split(",")
        rule_subset = get_rule_subset_2(rules, page_update_split)
        is_valid= is_page_valid_with_subset(rule_subset, page_update_split)

        if is_valid:
            middle_index = len(page_update_split) // 2
            middle_element = int(page_update_split[middle_index])
            update_sum = update_sum + middle_element

    print(update_sum)


def fix_update(rules: dict[str, list[str]], update: list[str]) -> list[str]:
    page_order: list[str] = update
    while(True):
        processed = []
        did_change = False
        for i in range(0, len(page_order)):
            value = page_order[i]
            value_rules = rules.get(value)
            if (value_rules == None): 
                processed.append(value)
                continue

            for j in range(0, len(processed)):
                p_value = processed[j]
                if p_value in value_rules:
                    page_order = removeElementAtIndex(page_order, i)
                    page_order = addElementAtIndex(page_order, j, value)
        
                    did_change = True
                    break
            processed.append(value)
        if not did_change:
            break
    return page_order

def solve_b(input: str):
    input_split = input.split("\n\n")
    rules = get_rules(input_split[0])
    page_updates = input_split[1].split("\n")
    update_sum = 0

    for page_update in page_updates:
        page_update_split = page_update.split(",")
        rule_subset = get_rule_subset_2(rules, page_update_split)
        is_valid = is_page_valid_with_subset(rule_subset, page_update_split)

        if not is_valid:
            new_order = fix_update(rule_subset, page_update_split)
            middle_index = len(new_order) // 2
            middle_element = int(new_order[middle_index])
            update_sum = update_sum + middle_element

    print(update_sum)


solve_a(data)
solve_b(data)