import os
import copy
import argparse
from datetime import datetime


def process_input(file_path):
    """
    Process the input file into the correct format
    :param file_path: the path of the file
    :return: the board, horizontal_dots, and vertical_dots as a tuple
    """
    try:
        file = open(file_path, "r")
    except FileNotFoundError:
        print("File not found")
        return

    content = file.read()
    content = content.split("\n\n")
    file.close()

    board = []
    board_temp = content[0].split("\n")
    for line in board_temp:
        curr_row = [int(elem) for elem in line.split()]
        board.append(curr_row)

    horizontal_dots = []
    dots_temp = content[1].split("\n")
    for line in dots_temp:
        curr_row = [int(elem) for elem in line.split()]
        horizontal_dots.append(curr_row)

    vertical_dots = []
    dots_temp = content[2].split("\n")
    for line in dots_temp:
        curr_row = [int(elem) for elem in line.split()]
        vertical_dots.append(curr_row)

    return board, horizontal_dots, vertical_dots


def check_assignment_complete(board):
    """
    Check whether the board is fully assigned
    :param board: The current board to check
    :return: boolean of whether the board assignment is complete
    """
    for row in board:
        for elem in row:
            if elem == 0:
                return False
    return True


def find_remaining_value(board_data, row, column):
    """
    Find the remaining possibilities for a given index on the board
    :param board_data: board and dots information
    :param row: row value to check
    :param column: column value to check
    :return: list of all possible remaining values
    """
    remaining_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    board = board_data[0]
    horizontal_dots = board_data[1]
    vertical_dots = board_data[2]

    # Check horizontal dots
    if column != 8 and horizontal_dots[row][column] != 0:  # Right dot
        if board[row][column + 1] != 0:
            total_numbers_allowed = []
            if horizontal_dots[row][column] == 1:
                number_allowed_lower = board[row][column + 1] - 1
                if 10 > number_allowed_lower > 0 and number_allowed_lower in remaining_values:
                    total_numbers_allowed.append(number_allowed_lower)
                number_allowed_higher = board[row][column + 1] + 1
                if 10 > number_allowed_higher > 0 and number_allowed_higher in remaining_values:
                    total_numbers_allowed.append(number_allowed_higher)
            else:
                number_allowed_half = board[row][column + 1] / 2
                if 10 > number_allowed_half > 0 and number_allowed_half % 1 == 0 and number_allowed_half in remaining_values:
                    total_numbers_allowed.append(int(number_allowed_half))
                number_allowed_double = board[row][column + 1] * 2
                if 10 > number_allowed_double > 0 and number_allowed_double % 1 == 0 and number_allowed_double in remaining_values:
                    total_numbers_allowed.append(int(number_allowed_double))

            if total_numbers_allowed:
                # Set the remaining values to just the numbers that satisfies the constraints
                remaining_values = total_numbers_allowed
            else:  # Dot constraint fails
                return []

    if column != 0 and horizontal_dots[row][column - 1] != 0:  # Left dot
        if board[row][column - 1] != 0:
            total_numbers_allowed = []
            if horizontal_dots[row][column - 1] == 1:
                number_allowed_lower = board[row][column - 1] - 1
                if 10 > number_allowed_lower > 0 and number_allowed_lower in remaining_values:
                    total_numbers_allowed.append(number_allowed_lower)
                number_allowed_higher = board[row][column - 1] + 1
                if 10 > number_allowed_higher > 0 and number_allowed_higher in remaining_values:
                    total_numbers_allowed.append(number_allowed_higher)
            else:
                number_allowed_half = board[row][column - 1] / 2
                if 10 > number_allowed_half > 0 and number_allowed_half % 1 == 0 and number_allowed_half in remaining_values:
                    total_numbers_allowed.append(int(number_allowed_half))
                number_allowed_double = board[row][column - 1] * 2
                if 10 > number_allowed_double > 0 and number_allowed_double % 1 == 0 and number_allowed_double in remaining_values:
                    total_numbers_allowed.append(int(number_allowed_double))

            if total_numbers_allowed:
                # Set the remaining values to just the numbers that satisfies the constraints
                remaining_values = total_numbers_allowed
            else:  # Dot constraint fails
                return []

    # Check vertical dots
    if row != 8 and vertical_dots[row][column] != 0:  # Bottom dot
        if board[row + 1][column] != 0:
            total_numbers_allowed = []
            if vertical_dots[row][column] == 1:
                    number_allowed_lower = board[row + 1][column] - 1
                    if 10 > number_allowed_lower > 0 and number_allowed_lower in remaining_values:
                        total_numbers_allowed.append(number_allowed_lower)
                    number_allowed_higher = board[row + 1][column] + 1
                    if 10 > number_allowed_higher > 0 and number_allowed_lower in remaining_values:
                        total_numbers_allowed.append(number_allowed_lower)
            else:
                number_allowed_half = board[row + 1][column] / 2
                if 10 > number_allowed_half > 0 and number_allowed_half % 1 == 0 and number_allowed_half in remaining_values:
                    total_numbers_allowed.append(int(number_allowed_half))
                number_allowed_double = board[row + 1][column] * 2
                if 10 > number_allowed_double > 0 and number_allowed_double % 1 == 0 and number_allowed_double in remaining_values:
                    total_numbers_allowed.append(int(number_allowed_double))

            if total_numbers_allowed:
                # Set the remaining values to just the numbers that satisfies the constraints
                remaining_values = total_numbers_allowed
            else:  # Dot constraint fails
                return []

    if row != 0 and vertical_dots[row - 1][column] != 0:  # Upper dot
        if board[row - 1][column] != 0:
            total_numbers_allowed = []
            if vertical_dots[row - 1][column] == 1:
                number_allowed_lower = board[row - 1][column] - 1
                if 10 > number_allowed_lower > 0 and number_allowed_lower in remaining_values:
                    total_numbers_allowed.append(number_allowed_lower)
                number_allowed_higher = board[row - 1][column] + 1
                if 10 > number_allowed_higher > 0 and number_allowed_higher in remaining_values:
                    total_numbers_allowed.append(number_allowed_higher)
            else:
                number_allowed_half = board[row - 1][column] / 2
                if 10 > number_allowed_half > 0 and number_allowed_half % 1 == 0 and number_allowed_half in remaining_values:
                    total_numbers_allowed.append(int(number_allowed_half))
                number_allowed_double = board[row - 1][column] * 2
                if 10 > number_allowed_double > 0 and number_allowed_double % 1 == 0 and number_allowed_double in remaining_values:
                    total_numbers_allowed.append(int(number_allowed_double))

            if total_numbers_allowed:
                # Set the remaining values to just the numbers that satisfies the constraints
                remaining_values = total_numbers_allowed
            else:  # Dot constraint fails
                return []

    # Check board

    block_row_start = (row // 3) * 3
    block_row_end = block_row_start + 2
    block_column_start = (column // 3) * 3
    block_column_end = block_column_start + 2

    for row_index in range(9):
        for column_index in range(9):
            board_number = board[row_index][column_index]
            # Check row
            if row_index == row:
                if board_number in remaining_values:
                    remaining_values.remove(board_number)
            # Check column
            if column_index == column:
                if board_number in remaining_values:
                    remaining_values.remove(board_number)
            # Check block:
            if block_row_start <= row_index <= block_row_end and block_column_start <= column_index <= block_column_end:
                if board_number in remaining_values:
                    remaining_values.remove(board_number)

    return remaining_values


def find_board_MRV(board_data):
    """
    Find the MRVs and remaining value matrix of the board
    :param board_data: board and the dots locations
    :return: All the MRV indexes and the remaining values matrix
    """
    board = board_data[0]
    remaining_values_matrix = []

    for row in range(9):
        remaining_values_line = []
        for column in range(9):
            if board[row][column] == 0:
                remaining_values_line.append(find_remaining_value(board_data, row, column))
            else:
                remaining_values_line.append("")
        remaining_values_matrix.append(remaining_values_line)

    MRV_index_list = []
    min_length = 10

    # Find MRV length
    for row in range(9):
        for column in range(9):
            if remaining_values_matrix[row][column] != "" and len(remaining_values_matrix[row][column]) < min_length:
                min_length = len(remaining_values_matrix[row][column])

    # Get index of all position that have the minimum length
    for row in range(9):
        for column in range(9):
            if len(remaining_values_matrix[row][column]) == min_length:
                MRV_index_list.append((row, column))

    return MRV_index_list, remaining_values_matrix


def find_board_degree_heuristic(board_data, MRV_index_list):
    """
    Find the degree heuristic for the board based on the MRV index list given
    :param board_data: board and dots information
    :param MRV_index_list: list of indexes to check
    :return: A list with all index with minimum degree heuristics
    """
    board = board_data[0]
    horizontal_dots = board_data[1]
    vertical_dots = board_data[2]

    degree_heuristic_data = []
    for row, column in MRV_index_list:
        curr_count = 0

        # Check horizontal dots
        if column + 1 <= 7 and horizontal_dots[row][column] != 0 and board[row][column + 1] == 0:  # Right dot
            curr_count += 1
        if column - 1 >= 0 and horizontal_dots[row][column - 1] != 0 and board[row][column - 1] == 0:  # Left dot
            curr_count += 1
        if row + 1 <= 7 and vertical_dots[row][column] != 0 and board[row + 1][column] == 0:  # Bottom dot
            curr_count += 1
        if row - 1 >= 0 and vertical_dots[row - 1][column] != 0 and board[row - 1][column] == 0:  # Upper dot
            curr_count += 1

        # Check board
        block_row_start = (row // 3) * 3
        block_row_end = block_row_start + 2
        block_column_start = (column // 3) * 3
        block_column_end = block_column_start + 2

        for row_index in range(9):
            for column_index in range(9):
                board_number = board[row_index][column_index]
                # Check row
                if row_index == row:
                    if board_number == 0:
                        curr_count += 1
                # Check column
                if column_index == column:
                    if board_number == 0:
                        curr_count += 1
                # Check block:
                if block_row_start <= row_index <= block_row_end and block_column_start <= column_index <= block_column_end:
                    if board_number == 0:
                        curr_count += 1

        degree_heuristic_data.append(curr_count)

    min_value = min(degree_heuristic_data)
    degree_heuristic_index_list = []

    for i in range(len(degree_heuristic_data)):
        if degree_heuristic_data[i] == min_value:
            degree_heuristic_index_list.append(MRV_index_list[i])

    return degree_heuristic_index_list


def forward_check(board_data, row, column, value):
    """
    Perform forward checking by pruning domains of neighbors based on the current assignment
    :param board_data: board and dots data
    :param row: row of the assigned value
    :param column: column of the assigned value
    :param value: the value being assigned
    :return: a dictionary with original domains for rollback or False if a constraint fails
    """
    board = board_data[0]
    horizontal_dots = board_data[1]
    vertical_dots = board_data[2]
    domains_backup = {}

    # Neighbors in same row
    for col in range(9):
        if col != column and board[row][col] == 0:
            domain = find_remaining_value(board_data, row, col)
            if value in domain:
                domain.remove(value)
                domains_backup[(row, col)] = domain[:]
                if not domain:
                    return False

    # Neighbors in same column
    for r in range(9):
        if r != row and board[r][column] == 0:
            domain = find_remaining_value(board_data, r, column)
            if value in domain:
                domain.remove(value)
                domains_backup[(r, column)] = domain[:]
                if not domain:
                    return False

    # Neighbors in same block
    block_row_start = (row // 3) * 3
    block_column_start = (column // 3) * 3
    for r in range(block_row_start, block_row_start + 3):
        for c in range(block_column_start, block_column_start + 3):
            if (r, c) != (row, column) and board[r][c] == 0:
                domain = find_remaining_value(board_data, r, c)
                if value in domain:
                    domain.remove(value)
                    domains_backup[(r, c)] = domain[:]
                    if not domain:
                        return False

    return domains_backup


def restore_domains(domains_backup, board_data):
    """
    Restore domains of variables after backtracking
    :param domains_backup: the original domains to restore
    :param board_data: board and dots data
    :return: None
    """
    board = board_data[0]
    for (row, column), domain in domains_backup.items():
        board[row][column] = 0


def backtrack(board_data):
    """
    Implementation of the backtracking algorithm using recurssion
    :param board_data: board and dots data
    :return: the result of the backtracking algorithm, false if no solution
    """
    board = board_data[0]
    if check_assignment_complete(board):
        return board

    MRV_index_list, remaining_values_matrix = find_board_MRV(board_data)

    # Degree Heuristic needed if 2+ variables
    if len(MRV_index_list) > 1:
        row, column = find_board_degree_heuristic(board_data, MRV_index_list)[0]
    else:
        row, column = MRV_index_list[0]

    domain = remaining_values_matrix[row][column]

    # No forward checking
    # for value in domain:
    #     board[row][column] = value
    #     result = backtrack(board_data)
    #     if result:
    #         return result
    #     board[row][column] = 0

    # With forward checking
    for value in domain:
        board[row][column] = value

        domains_backup = forward_check(board_data, row, column, value)
        if domains_backup is not False:
            result = backtrack(board_data)
            if result:
                return result

            # If backtracking occurs restore domains
            restore_domains(domains_backup, board_data)

        board[row][column] = 0

    return False


def process_output(file_path, result):
    """
    Put the result into an output file
    :param file_path: the path of the output file
    :param result: the result produced by the algorithm
    :return: None
    """
    file = open(file_path, "w")
    for line in result:
        for elem in line:
            print(elem, end=" ", file=file)
        print(file=file)


def main():
    parser = argparse.ArgumentParser(description='Solve a Kropki Sudoku puzzle.')
    parser.add_argument("input_file", type=str, help="Input file from the Inputs folder")
    parser.add_argument(
        "-o", "--output_file", type=str, help="Name of the output file to be saved in the Outputs folder"
    )
    args = parser.parse_args()

    input_path = os.path.join("Inputs", args.input_file)

    if args.output_file:
        output_path = os.path.join("Outputs", args.output_file)
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d__%H-%M-%S")
        output_path = os.path.join("Outputs", f"{timestamp}__Output.txt")

    board_data = process_input(input_path)
    if not board_data:
        print(f"Could not process input file '{args.input_file}'")
        return
    
    result = backtrack(board_data)
    if not result:
        print("No solution found")
    else:
        process_output(output_path, result)
        print(f"Solution saved to '{output_path}'")


if __name__ == "__main__":
    main()
