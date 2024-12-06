from aocd import data
from enum import Enum

example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class GridState(Enum):
    FREE = 0
    BLOCKED = 1
    EXIT = 2
    GUARD = 3

def rotate(current_direction: Direction) -> Direction:
    new_direction_value = (current_direction.value + 1) % len(Direction)
    return Direction(new_direction_value)

def parse_map(input: str) -> list[str]:
    return input.split("\n")


def get_coordinate_state(map: list[str], n: int, m: int) -> GridState:
    if (n < 0 or m < 0):
        return GridState.EXIT
    if (n >= len(map) or m >= len(map[0])):
        return GridState.EXIT
    if (map[n][m] == "."):
        return GridState.FREE
    if (map[n][m] == "#"):
        return GridState.BLOCKED
    if (map[n][m] == "^"):
        return GridState.GUARD

def get_direction_move_state(map: list[str], n: int, m: int, direction: Direction) -> GridState:
    new_n = None
    new_m = None
    if direction == Direction.UP:
        new_n = n - 1
        new_m = m
    if direction == Direction.RIGHT:
        new_n = n
        new_m = m + 1
    if direction == Direction.DOWN:
        new_n = n + 1
        new_m = m
    if direction == Direction.LEFT:
        new_n = n
        new_m = m - 1
    return get_coordinate_state(map, new_n, new_m)   

def find_guard_position(map: list[str]) -> tuple[str, str]:
    for n in range(0, len(map)):
        for m in range(0, len(map[0])):
            if get_coordinate_state(map, n, m) == GridState.GUARD:
                return (n, m)

def move(position: tuple[int, int], direction: Direction) -> tuple[int, int]:
    new_n = None
    new_m = None

    n = position[0]
    m = position[1]

    if direction == Direction.UP:
        new_n = n - 1
        new_m = m
    if direction == Direction.RIGHT:
        new_n = n
        new_m = m + 1
    if direction == Direction.DOWN:
        new_n = n + 1
        new_m = m
    if direction == Direction.LEFT:
        new_n = n
        new_m = m - 1
    return (new_n, new_m)

def solve_a(input: str):
    map = parse_map(input)

    position = find_guard_position(map)

    n = position[0]
    m = position[1]

    # Remove guard position from the map
    row_as_list = list(map[n])
    row_as_list[m] = "."
    map[n] = ''.join(row_as_list) 

    direction = Direction.UP

    guard_positions: set[tuple[int, int]] = set()
    guard_positions.add(position)

    while(True):
        aimed_grid_state: GridState = get_direction_move_state(map, position[0], position[1], direction)

        if (aimed_grid_state == GridState.FREE):
            position = move(position, direction)
            guard_positions.add(position)
        if (aimed_grid_state == GridState.BLOCKED):
            direction = rotate(direction)
        if (aimed_grid_state == GridState.EXIT):
            break

    print("solve (a): " + str(len(guard_positions)))


def print_map(map: list[str], guard_positions: set[tuple[int, int, Direction]]) -> None:
    map_copy = [list(row) for row in map]
    for guard_position in guard_positions:
        x, y, _ = guard_position
        if 0 <= x < len(map_copy) and 0 <= y < len(map_copy[0]):
            map_copy[x][y] = 'X'
    for row in map_copy:
        print("".join(row))

def solve_b(input: str):
    map = parse_map(input)
    position = find_guard_position(map)

    # Save initial positions
    n = position[0]
    m = position[1]

    # Memove guard position from the map (mark it as a free spot)
    row_as_list = list(map[n])
    row_as_list[m] = "."
    map[n] = ''.join(row_as_list) 

    obstacle_loop_count = 0
    for i in range(0, len(map)):
        print(str(i) + " / " + str(len(map)))
        for j in range(0, len(map[0])):
            # Initial position cannot have blockage
            if i == n and j == m:
                continue
            
            # Reset position and direction
            position = (n, m)
            direction = Direction.UP

            # Initialize guard positions and add the initial position
            guard_positions: set[tuple[int, int, Direction]] = set()
            guard_positions.add( (position[0], position[1], direction) )

            # Add the new blockage
            new_map = [list(row) for row in map]
            row_as_list = list(new_map[i])
            row_as_list[j] = "#"
            new_map[i] = ''.join(row_as_list)

            # Play the guard's lifecycle
            while(True):
                aimed_grid_state: GridState = get_direction_move_state(new_map, position[0], position[1], direction)

                if (aimed_grid_state == GridState.FREE):
                    position = move(position, direction)

                    # If this position & direction have already been visited it means we are in a loop
                    if ((position[0], position[1], direction) in guard_positions):
                        obstacle_loop_count = obstacle_loop_count + 1
                        break

                    guard_positions.add( (position[0], position[1], direction) )
                if (aimed_grid_state == GridState.BLOCKED):
                    direction = rotate(direction)
                if (aimed_grid_state == GridState.EXIT):
                    break
    print("solve (a): " + str(obstacle_loop_count))

solve_a(data)
solve_b(data)