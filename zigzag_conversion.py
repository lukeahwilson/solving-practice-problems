#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-01
# Question:
#       The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
#       (you may want to display this pattern in a fixed font for better legibility)
# Example:
#       Input: s = "PAYPALISHIRING", numRows = 4
#       Output: "PINALSIGYAHRPI"
#       Explanation:
#       P     I    N
#       A   L S  I G
#       Y A   H R
#       P     I
# Constraints:
#       1 <= s.length <= 1000
#       s consists of English letters (lower-case and upper-case), ',' and '.'.
#       1 <= numRows <= 1000

# Brainstorm...

# Brute force: (O(n^2))
    # Create 2d matrix by len(s)/numrows + roundup = numcols    (O(n?))
    # For character in string, input to matrix and step         (O(n))
        # If down is True, walk down,
        # If True and bottom, set down to False
        # If down is False walk upward and rightward
        # If False and top, set down to True
    # When complete start new for loop on 2d matrix             (O(n))
        # If blank, skip index on matrix and go to next         (O(n))
        # If character (not blank) append to new string
        # When complete, return the new string

# Fast: (O(nk))
    # Create dictionary of characters (O(1))
        # Key is the character
        # Value is index of characters on an imaginary 2d grid
    # For loop to add key-value pairs to the dictionary O(n)
        # If down is True, walk down,
        # If True and bottom, set down to False
        # If down is False walk upward and rightward
        # If False and top, set down to True
    # When complete start new for loop on 2d matrix             (O(n))
        # For loop by columns
        # If doesn't exist, skip index on matrix and go to next         (O(1)? maybe O(nk))
        # If character exists append to new string
        # When complete, return the new string

# Faster: (O(n))
    # Create new string of characters (O(n))
    # algorithmically calculate indicies to append from original string
    # For loop down rows to build new processed string row by row (O(n))
        # For loop across cols to build new row strings letter by letter
            # If index % (numrows-row-2)
                # Append s[index] to rowstring
        # Append rowstring to new string

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        processed_string = ''
        max_zags = len(s) // numRows + 1
        zag_length = (numRows-1)*2
        row_number = 0
        if numRows == 1:
            zag_length = 1

        # print(s)
        # print(max_zags)
        # print(numRows)
        # print(zag_length)

        while row_number < numRows:
            zag_2_offset = row_number*2
            zag_number = 0
            str_number = 0
            processed_row = ''
            while zag_number < max_zags:

                string_index = zag_length*zag_number + row_number

                if row_number not in [0, numRows-1] and zag_number > 0 and (string_index - zag_2_offset) < len(s):
                    processed_row += s[string_index - zag_2_offset]

                if string_index < len(s):
                    processed_row += s[string_index]

                if numRows >= len(s):
                    zag_number = max_zags

                # print()
                # print('Row #', row_number)
                # print('Zag #', zag_number)
                # print('Str Index =', string_index)
                # print('Processed Row = \'', processed_row, '\'')

                zag_number += 1

            row_number += 1
            processed_string += processed_row

        return processed_string
