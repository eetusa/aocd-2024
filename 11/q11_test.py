from q11 import parse_input, add_to_map, get_map_total, blink, solve

def test_parse_input():
    input_str = "0 1 10 99 999 10 0"
    expected_output = {0: 2, 1: 1, 10: 2, 99: 1, 999: 1}
    assert parse_input(input_str) == expected_output

def test_add_to_map():
    stone_map = {0: 1, 1: 2}
    add_to_map(stone_map, 1, 1)
    add_to_map(stone_map, 2, 3)
    assert stone_map == {0: 1, 1: 3, 2: 3}

def test_get_map_total():
    stone_map = {0: 1, 1: 2, 2: 3}
    assert get_map_total(stone_map) == 6

def test_blink():
    initial_stone_map = {125: 1, 17: 1}
    blink_count = 1
    assert blink(initial_stone_map, blink_count) == 3

    blink_count = 6
    assert blink(initial_stone_map, blink_count) == 22

def test_solve():
    input_str = "125 17"
    blink_count = 6
    excercise = "example"
    assert solve(input_str, blink_count, excercise) == 22