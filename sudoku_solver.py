board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
# [row][column]


def solve(bo):
    # base case
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        # add values 1 - 9
        if vaild(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            # backtracking 
            # reset last element added 
            bo[row][col] = 0

    return False


def vaild(bo, num, pos):

    # Check row
    for i in range(len(bo[0])):
            # loop through every column
            # check if == to what number we just added in 
                                        # dont check position we just added 
            if bo[pos[0]][i] == num and pos[1] != i:
                return False

    # Check column
    for i in range(len(bo)):
        # not the extsct position we entered
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # loop through box
    # find what box we are in multpuly by 3
    for i in range(box_y * 3, box_y*3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


print_board(board)
solve(board)
print('************************************')
print_board(board)
