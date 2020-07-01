from utils import *


def search2(values):
    "Using depth-first search and propagation, try all possible values."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False  ## Failed earlier
    if is_solved(values):
        return values  ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    chosen_one = temp(values)
    possibilities = values[chosen_one]
    # n, s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and
    for possibility in possibilities:
        new_sudoku = values.copy()
        new_sudoku[chosen_one] = possibility
        new_values = search(new_sudoku)
        if new_values:
            return new_values
    # If you're stuck, see the solution.py tab!


def search(values):
    "Using depth-first search and propagation, try all possible values."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False  ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes):
        return values  ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n, s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt


valuess = {'E4': '359', 'F5': '1', 'B7': '12679', 'E7': '4', 'A1': '4', 'A6': '269', 'D2': '2', 'B6': '245689',
           'B3': '1256789', 'H2': '6789', 'I8': '23589', 'E1': '3679', 'I9': '23689', 'B5': '24569', 'E3': '15679',
           'G7': '1259', 'A8': '1239', 'F7': '23579', 'D6': '4579', 'C4': '7', 'C8': '12349', 'F9': '23789',
           'D1': '3789', 'G5': '459', 'F6': '25679', 'C1': '2689', 'B1': '26789', 'G2': '89', 'H4': '2', 'E8': '12359',
           'E2': '15679', 'H5': '479', 'H8': '489', 'I5': '579', 'D9': '13789', 'H3': '3', 'H6': '1', 'G9': '12489',
           'C3': '125689', 'I3': '4', 'H7': '69', 'D3': '15789', 'C9': '123469', 'A7': '8', 'H1': '5', 'A5': '2369',
           'E9': '12379', 'F4': '359', 'B9': '124679', 'E5': '8', 'F3': '56789', 'F2': '4', 'F8': '23589', 'G4': '6',
           'I1': '1', 'G6': '3', 'B2': '3', 'I2': '6789', 'A3': '12679', 'C7': '12369', 'E6': '25679', 'I6': '5789',
           'A4': '139', 'C2': '15689', 'A9': '5', 'I7': '23569', 'D7': '13579', 'G3': '289', 'F1': '36789', 'G8': '7',
           'D5': '34579', 'B4': '14589', 'G1': '289', 'C6': '245689', 'H9': '4689', 'C5': '234569', 'D4': '3459',
           'D8': '6', 'B8': '1249', 'A2': '1679', 'I4': '589'}
display(search2(valuess))
