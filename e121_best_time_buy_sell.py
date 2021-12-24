#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-24
# Question:
#       You are given an array prices where prices[i] is the price of a given stock on the ith day.
#   You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
#   future to sell that stock.
# Example:
#       Input: prices = [7,1,5,3,6,4]
#       Output: 5
#       Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#       Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Constraints:
#       1 <= prices.length <= 105
#       0 <= prices[i] <= 104
##

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_past = inf
        max_gain = 0

        for index in range(len(prices)):
            if min_past > prices[index]:
                min_past = prices[index]

            if prices[index] - min_past > max_gain:
                max_gain = prices[index] - min_past

        return max_gain
