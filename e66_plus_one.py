#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-25
# Question:
#       You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
#   The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Example:
#       Input: digits = [1,2,3]
#       Output: [1,2,4]
#       Explanation: The array represents the integer 123.
#       Incrementing by one gives 123 + 1 = 124.
#       Thus, the result should be [1,2,4].
# Constraints:
#       1 <= digits.length <= 100
#       0 <= digits[i] <= 9
#       digits does not contain any leading 0's.
##

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0

        print('Digits', digits, 'Let\'s Add 1!\n')

        for i in range(len(digits) - 1, -1, -1):
            print('Index', i)
            print('Digit', digits[i])

            if i == len(digits) - 1:
                digits[i] += 1

            if carry:
                digits[i] += 1
                carry = 0

            print('Change', digits[i])
            print('Digits', digits)

            if digits[i] == 10:
                digits[i] = 0
                carry = 1
            else:
                print('No Carry')
                break

            print('Carry', carry)
            print()


        if carry:
            digits = [1] + digits
            print('New Significant Digit')

        print('Final Result', digits)

        print('\n---------------------\n')

        return digits
