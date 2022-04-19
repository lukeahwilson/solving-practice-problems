#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-04-18
# Question: https://www.hackerrank.com/challenges/find-the-running-median/problem
##

def runningMedian(a):
    # Write your code here

    run_list = []
    median_list = []

    for char in a:
        mid = 0
        if len(run_list) > 0:
            left = 0
            right = len(run_list)
            while left <= right:
                mid = (left + right) // 2
                print(left, right, mid)
                if run_list[mid] == char:
                    break
                if run_list[mid] < char:
                    print(mid, run_list[mid], 'Char greater than mid')
                    left = mid + 1
                if run_list[mid] > char:
                    print(mid, run_list[mid], 'Char less than mid')
                    right = mid - 1

        run_list = run_list[:mid] + [char] + run_list[mid:len(run_list)]

        length = len(run_list) - 1
        center =  length // 2
        bisect = length % 2

        if bisect:
            median = (run_list[center] + run_list[center + bisect])/2
        else:
            median = run_list[center]

        print('Char', char)
        print('RunList', run_list)
        print('Mid-Index', mid)
        print('Median', median)

        median_list.append(median)

    return median_list
