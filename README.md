# Kropki Sudoku Solver

This project is a Kropki Sudoku solver built using a backtracking algorithm with specific heuristics to optimize variable selection. The solver aims to fill a 9x9 grid with numbers from 1 to 9 while satisfying traditional Sudoku constraints, as well as additional Kropki-specific constraints.

## Project Overview

Kropki Sudoku adds two unique rules to the standard Sudoku:
1. **White Dots**: If a white dot exists between two adjacent cells, one cell must contain a number that is exactly 1 greater than the other.
2. **Black Dots**: If a black dot exists between two adjacent cells, one cell must contain a number that is exactly double the other.

### Goal
The objective is to solve the puzzle by assigning values to each cell in a way that:
- Each row, column, and 3x3 sub-grid contains the numbers 1 through 9 exactly once.
- White and black dot constraints between adjacent cells are satisfied.

## Project Structure

- `sudoku_solver.py`: Main implementation of the Kropki Sudoku solver.
- `Inputs/`: Folder containing input files.
- `Outputs/`: Folder where the solution files are saved.
- `README.md`: Documentation.

## Implementation Details

1. **Backtracking Algorithm**: This uses the Minimum Remaining Values (MRV) and Degree Heuristics for variable selection.
2. **Domain Ordering**: Domain values are ordered from 1 to 9.
3. **Constraints**: Implemented to ensure Sudoku, white dot, and black dot rules.
4. **Inference**: Utilizes Forward Checking to improve performance.

## Input/Output Format

### Input Format
1. **Initial Board State**: A 9x9 grid, where each cell has a number from 0 (empty) to 9.
2. **Horizontal Dots**: Specifies white and black dots between horizontally adjacent cells (1 for white, 2 for black, 0 for none).
3. **Vertical Dots**: Specifies dots for vertically adjacent cells in the same format as above.

### Output Format
The solution is a 9x9 grid with values from 1 to 9, satisfying all constraints.

## Running the Program

### Prerequisites
- Python 3.7 or higher

### Steps
1. Place your input file in the `Inputs` folder.
2. Run the solver using the following command:
   ```bash
   python sudoku_solver.py <input_file> [-o <output_file>]