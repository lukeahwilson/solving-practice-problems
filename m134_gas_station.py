#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-04-14
# Question: https://leetcode.com/problems/gas-station/
##

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        start = 0
        end = start + 1
        tank = gas[start] - cost[start]

        while end != start:
            if tank < 0:
                start -= 1
                if start < 0: start = len(gas) + start
                tank += gas[start] - cost[start]
            else:
                if end >= len(gas): end = -1
                tank += gas[end] - cost[end]
                end += 1
        return start

#       Situation
# n gas stations on circular route
# gas quantity at a ith is gas[i]
# car with unlimited tank
# cost to go from ith to next (i + 1)th station is cost[i]
# start empty at one of the stations
# can only drive clockwise (left to right)

#       Problem
# given two integer arrays, gas and cost
# return the starting gas stations index if you can travel around the circuit once
# return -1 if it isn't possible, there will only be one solution

#       Notes
# no optimization required since unlimited gas tank and minimum gas is always simply the sum of the costs for one cycle

#       Questions I'd Ask (no one to answer them)
# Is it a magic station that could return negative cost (this shouldn't change anything if you think about it)

#       Resources
# summing total gas and comparing to total cost
#   because of how heavily constrained the problem is, this seems to solve whether it is possible or not

#       Challenges
# how do we figure out which index to start at?
# how do we circle around the array back to start?

#       Edge Case Concerns
# All cost one location?
# All gas one location

#       Ideas
# summing total gas and comparing to total cost to confirm possible
# brute force method:
#   - start at station 1, fill up, subtract, repeat through and check if tank goes negative
#   - repeat for subsequent stations until one of them successfully works
#   - concern here is O(n^2) as we need to walk twice
#   - Note: if we traverse a bunch of stations in a row and then fail,
#   - Note: we already know they can be traversed, no need to start over at next station
#   - Note: this reminds me of a longest consecutive sequence problem,
#   - Note: where we step forward and if we error out, we remove first and try again

# more efficient method:
#   - start at a station, fill up, subtract, repeat until failure
#   - drop starting location, check if the tank improves
#   - Note: don't drop start location, that was net positive or it would have failed
#   - Note: scratch previous analogy it's more like a sorted two sum two pointer that walks outward as opposed to inward
# iterating on above idea:
#   - instead lets add station from before and see if it enables us to move forward
#   - if no improvement, continue to walk backwards, if improvement, walk forwards until problem
#   - this should work until a solution is found

#       Plan
#   - start at a station with end at next station
#   - fill up start gas, subtract start cost
#   Loop:
#   - check if positive
#   - if positive, fill up at end, subtract cost at end, and move the finish out one
#   - if negative, move start backward one and fill up there, subtract cost at start location

#       Demo Run
# start at 0 end at 1
# tank = 0, use start
# tank = 1 - 3 = -2

# tank negative
# start at -1 = 4, end at 1
# tank = 5 - 2 + (-2) = 1

# tank positive
# start at 4, end at 2
# tank = 2 - 4 + (1) = -1

# tank negative
# start at 3, end at 2
# tank = 4 - 1 + (-1) = 2

# tank positive
# start at 3 end at 3 # Note that the start is negative and while loop never ends, so need to fix this, use not equal
# tank = 3 - 5 + (2) = 0

# Script ends, start location is 3

#       Demo Run
# start at 0 end at 1
# tank = 0, use start
# tank = 5 - 4 = 1

# tank positive
# start at 0, end at 2
# tank = 1 - 4 + (1) = -2

# tank negative
# start at -1 = 4, end at 2
# tank = 4 - 1 + (-2) = 1

# tank positive
# start at 4, end at 3
# tank = 2 - 1 + (1) = 2

# tank positive
# start at 4 end at 4
# tank = 3 - 5 + (2) = 0

# Script ends, start location is 4
