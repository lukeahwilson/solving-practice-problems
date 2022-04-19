#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-04-19
##

max_distance = 11000
forward = [[1,3000],[2,5000],[3,4000],[4,10000],[5,8000]]
backward = [[1,1000],[2,3000],[3,4000]]

def optimal_flight(forward, backward, max_distance):

    forward = sorted(forward, key=lambda x: x[1]) #O(nlogn)
    backward = sorted(backward, key=lambda x: x[1]) #O(mlogm)
    left = 0
    right = len(backward) - 1
    distance = 0
    optimal_flights = []

    while left < len(forward) and right >= 0:
        if forward[left][1] + backward[right][1] > max_distance:
            right -= 1
        elif forward[left][1] + backward[right][1] > distance:
            distance = forward[left][1] + backward[right][1]
            optimal_flights = [[forward[left][0], backward[right][0]]]
            left += 1
        elif forward[left][1] + backward[right][1] == distance:
            optimal_flights.append([forward[left][0], backward[right][0]])
            left += 1
        else:
            left += 1

    return optimal_flights

if __name__ == '__main__':
    print(optimal_flight(forward, backward, max_distance))
