#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-01-10
# Question:
#       Determine if a 9 x 9 Sudoku board is valid.
# Constraints:
#       board.length == 9
#       board[i].length == 9
#       board[i][j] is a digit 1-9 or '.'.
##

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_row_hash = defaultdict(set)
        valid_col_hash = defaultdict(set)
        valid_sqr_hash = defaultdict(set)

        for r_x in range(3):
            for c_x in range (3):
                for row in range(3*r_x, 3+3*r_x):
                    for col in range(3*c_x, 3+3*c_x):
                        if board[row][col] == '.':
                            continue
                        if (board[row][col] in valid_row_hash[row]
                            or board[row][col] in valid_col_hash[col]
                            or board[row][col] in valid_sqr_hash[c_x + 3*r_x]):
                            return False
                        valid_row_hash[row].add(board[row][col])
                        valid_col_hash[col].add(board[row][col])
                        valid_sqr_hash[c_x + 3*r_x].add(board[row][col])

        return True
