from aocd import data

# matrix[n][m]
#
#  n
#m 1 2 3
#  2
#  3

test = """123XMAS
12XMAS3
1XMAS23
XMAS123
AS123XM"""

test2 = """123SAMX
12SAMX3
1SAMX23
SAMX123
AMX123S"""

test3 = """XMAS123
MAS123X
AS123XM
S123XMA
123XMAS"""

test4 = """XMAS123
111A22S
111M11A
111X11M
111X11X"""

test5 = """XXASS23
1MXA22S
11AM11S
111SA1X
111X1SX"""

example = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

# Straight directions
def is_xmas_left_right(matrix: list[list[str]], n: int, m: int, width, height):
    if (width - m < 4):
        return False
    if matrix[n][m+1] == "M" and matrix[n][m+2] == "A" and matrix[n][m+3] == "S":
        return True
    return False

def is_xmas_right_left(matrix: list[list[str]], n: int, m: int, width, height):
    if (m < 3):
        return False
    if matrix[n][m-1] == "M" and matrix[n][m-2] == "A" and matrix[n][m-3] == "S":
        return True
    return False

def is_xmas_up_down(matrix: list[list[str]], n: int, m: int, width, height):
    if (height - n < 4):
        return False
    if matrix[n+1][m] == "M" and matrix[n+2][m] == "A" and matrix[n+3][m] == "S":
        return True
    return False

def is_xmas_down_up(matrix: list[list[str]], n: int, m: int, width, height):
    if (n < 3):
        return False
    if matrix[n-1][m] == "M" and matrix[n-2][m] == "A" and matrix[n-3][m] == "S":
        return True
    return False

# Diagonals

def is_xmas_left_right_up_down(matrix: list[list[str]], n: int, m: int, width, height):
    if (width - m < 4):
        return False
    if (height - n < 4):
        return False
    if matrix[n+1][m+1] == "M" and matrix[n+2][m+2] == "A" and matrix[n+3][m+3] == "S":
        return True
    return False

def is_xmas_left_right_down_up(matrix: list[list[str]], n: int, m: int, width, height):
    if (width - m < 4):
        return False
    if (n < 3):
        return False
    if matrix[n-1][m+1] == "M" and matrix[n-2][m+2] == "A" and matrix[n-3][m+3] == "S":
        return True
    return False

def is_xmas_right_left_up_down(matrix: list[list[str]], n: int, m: int, width, height):
    if (m < 3):
        return False
    if (height - n < 4):
        return False
    if matrix[n+1][m-1] == "M" and matrix[n+2][m-2] == "A" and matrix[n+3][m-3] == "S":
        return True
    return False

def is_xmas_right_left_down_up(matrix: list[list[str]], n: int, m: int, width, height):
    if (m < 3):
        return False
    if (n < 3):
        return False
    if matrix[n-1][m-1] == "M" and matrix[n-2][m-2] == "A" and matrix[n-3][m-3] == "S":
        return True
    return False

def is_x_mas(matrix: list[list[str]], n: int, m: int, width, height):
    if (n < 1):
        return False
    if (m < 1):
        return False
    if (width - m < 2):
        return False
    if (height - n < 2):
        return False
    
    left_diagonal = False
    right_diagonal = False
    
    if matrix[n-1][m-1] == "M":
        if matrix[n+1][m+1] == "S":
            left_diagonal = True
    if matrix[n-1][m-1] == "S":
        if matrix[n+1][m+1] == "M":
            left_diagonal = True
    if matrix[n+1][m-1] == "M":
        if matrix[n-1][m+1] == "S":
            right_diagonal = True
    if matrix[n+1][m-1] == "S":
        if matrix[n-1][m+1] == "M":
            right_diagonal = True

    return left_diagonal == True and right_diagonal == True

def count_xmas_in_coordinate(matrix: list[list[str]], n: int, m: int, width, height):
    count = 0
    if (is_xmas_left_right(matrix, n, m, width, height)):
        count = count + 1
    if (is_xmas_right_left(matrix, n, m, width, height)):
        count = count + 1
    if (is_xmas_up_down(matrix, n, m, width, height)):
        count = count + 1
    if (is_xmas_down_up(matrix, n, m, width, height)):
        count = count + 1
    if (is_xmas_left_right_up_down(matrix, n, m, width, height)):
        count = count + 1
    if (is_xmas_left_right_down_up(matrix, n, m, width, height)):
        count = count + 1
    if (is_xmas_right_left_down_up(matrix, n, m, width, height)):
        count = count + 1
    if (is_xmas_right_left_up_down(matrix, n, m, width, height)):
        count = count + 1
    return count

def solve_a(input):
    matrix = input.split("\n")
    width = len(matrix[0])
    height = len(matrix)
    sum = 0

    for n in range(0, height):
        for m in range(0, width):
            if matrix[n][m] == "X":
                sum = sum + count_xmas_in_coordinate(matrix, n, m, width, height)
    print("solve (a): " + str(sum))

def solve_b(input):
    matrix = input.split("\n")
    width = len(matrix[0])
    height = len(matrix)
    sum = 0

    for n in range(0, height):
        for m in range(0, width):
            if matrix[n][m] == "A":
                sum = sum + is_x_mas(matrix, n, m, width, height)
    print("solve (b): " + str(sum))


solve_a(data)
solve_b(data)