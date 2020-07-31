import copy

"""Takes user input on board dimension, initializes the board and collects the target to track and number of turns"""

board_size = input("Please insert your board size as X, Y: ").split(", ")
columns, rows = int(board_size[0]), int(board_size[1])
board = []

for i in range(rows):  # takes input on initial state as string on each line
    gen_zero = input(f"Please insert Generation Zero for row {i + 1}: ")
    gen_zero = [j for j in gen_zero]  # turn each line of input into a list
    board.append(gen_zero)  # append to board to create 2D Matrix

target = input("Please insert target location and number of turns as X, Y, N: ").split(", ")
target_y, target_x, turns = int(target[1]), int(target[0]), int(target[2])


"""Check if there are elements in top-left, top-center and top-right and add 1 point for each existing green neighbour
to the counter. Return the number of green neighbours."""


def check_top(matrix, y, x):
    top_neighbours = 0
    if x - 1 >= 0:
        if matrix[y - 1][x - 1] == "1":
            top_neighbours += 1
    if matrix[y - 1][x] == "1":
        top_neighbours += 1
    if x + 1 < len(board[y]):
        if matrix[y - 1][x + 1] == "1":
            top_neighbours += 1

    return top_neighbours


"""Check if there are elements on the left and right sides and add 1 point for each existing green neighbour
to the counter. Return the number of green neighbours."""


def check_sides(matrix, y, x):
    side_neighbours = 0
    if x - 1 >= 0:
        if matrix[y][x - 1] == "1":
            side_neighbours += 1
    if x + 1 < len(matrix[y]):
        if matrix[y][x + 1] == "1":
            side_neighbours += 1

    return side_neighbours


"""Check if there are elements in bottom-left, bottom-center and bottom-right and add 1 point for each existing green
neighbour to the counter. Return the number of green neighbours."""


def check_bottom(matrix, y, x):
    bottom_neighbours = 0
    if x - 1 >= 0:
        if matrix[y + 1][x - 1] == "1":
            bottom_neighbours += 1
    if matrix[y + 1][x] == "1":
        bottom_neighbours += 1
    if x + 1 < len(matrix[y]):
        if matrix[y + 1][x + 1] == "1":
            bottom_neighbours += 1

    return bottom_neighbours


"""Check if the current element is RED or GREEN and if it has the required amount of GREEN neighbours to change its
color. Return the new color"""


def switch(element, total_neighbours):
    if element == "0":
        if total_neighbours in [3, 6]:
            new_element = "1"
        else:
            new_element = element
    else:
        if total_neighbours in [0, 1, 4, 5, 7, 8]:
            new_element = "0"
        else:
            new_element = element

    return new_element


"""Take the board as argument and call the 3 check functions and the switch function. Return the number of times the
target has remained GREEN for N turns"""


def main(board):
    green_control = 0  # initialize counter for the number of turns target was green
    for turn in range(turns):  # for every turn
        if board[target_y][target_x] == "1": # first check if Gen 0 target status is green
            green_control += 1
        temp_board = copy.deepcopy(board)  # each turn create a copy of the latest board
        for y in range(len(board)):  # traverse the grid from top to bottom
            for x in range(len(board[y])):  # traverse left to right
                if y - 1 >= 0:  # check if elements exist to the top
                    top_neighbours = check_top(board, y, x)  # check for green neighbours to the top side
                else:
                    top_neighbours = 0
                side_neighbours = check_sides(board, y, x)  # check left and right green neighbours on same line
                if y + 1 < len(board):  # check if elements exist to the bottom
                    bottom_neighbours = check_bottom(board, y, x)  # check for green neighbours to the bottom side
                else:
                    bottom_neighbours = 0
                total_neighbours = top_neighbours + side_neighbours + bottom_neighbours # sum all neighbours for element
                temp_board[y][x] = switch(board[y][x], total_neighbours)  # switch color if condition fulfilled

        board = copy.deepcopy(temp_board)  # copy the result and prepare board for next turn

    if board[target_y][target_x] == "1":  # check if target is green the final generation
        green_control += 1
    return green_control

print(main(board))