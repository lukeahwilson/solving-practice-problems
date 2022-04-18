#!/usr/bin/python
# PROGRAMMER: Luke Wilson
##

'''
Binary Search: This is possible on sorted lists!
- Works by creating a left and right pointer at the beginning and end
- Check the value at the middle by taking the average of the left and right pointers
- If the middle is the target, return the target.
- If the middle is too large, set right pointer to middle - 1 (as mid and all above nums are larger)
- Otherwise if the middle is too small, set the left pointer to middle + 1
- Repeat this process until the target is found, or the search completes and there is no target
- There is no target if the left and right pointers cross eachother
'''
class Solution:
    def binarysearch(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2 (# we floor divide for integer, (left + right + 1) also works)
            if nums[mid] == target: return mid
            if target < nums[mid]: right = mid -1
            else: left = mid + 1
        return -1

# Example of using binary search to find a pivot and then a follow up search in the new area
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            center = (left + right) // 2
            if nums[center] < nums[0]: right = center - 1
            else: left = center + 1

        if nums[0] <= target: left = 0
        else: right = len(nums) - 1

        while left <= right:
            center = (left + right) // 2
            if nums[center] < target: left = center + 1
            elif nums[center] > target: right = center - 1
            else: return center
        return -1
"""
MergeSort is much more simple to implement than QuickSort. There is no amortized worst case,
however we need to store our matrix in a second data structure requiring O(n) extra memory.
    It works by recursively dividing the array into smaller sub arrays.
    Once at the bottom, it sorts the sub arrays one at a time
    It then tunnels up one level at a time and sorts the larger array each time
    Think of it as merging two sorted linked lists into a new sorted linked list
"""
def mergeSort(arr):
    if len(arr) > 1:
         # Finding the mid of the array and divide the array into two halves
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        # Recursive calls on left and right halves of the array
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
"""
QuickSort is a bit more complex. It is very efficient O(nlogn)
    With worst case pivot choices it is slower at O(n^2)
    Consider that comparing all numbers with eachother is O(n^2).
    Every pivot would need to be perfectly bad.
    It works by taking your array, entering with the outer bounds of the array, and picking a pivot
    It then moves all numbers less than the pivot below it, and numbers greater than, above it
    The result is the pivot in the correct location. We return the pivot location to act as new outer bounds
    Now we recursively call the quicksort function on the sub-arrays, using the pivot as the outer bounds
    Slowly smaller and smaller arrays get sorted, until the array is one element long, at which point it returns
    The partition function works by incrementing through the array with two pointers both at start
    When a number is less than the array, we increment i, and swap j and i locations
    By the end, all numbers below the pivot are to the left, and all above pivot to the right
    We finish by swapping the lowest of the high with the pivot to place the pivot in the middle
    Then we return the pivot
"""
# QuickSort Functions
def quickSort(arr, low, high):
    if len(arr) == 1:   # then all we have is the partition which is in right spot
        return arr      # return the single element array (partition) to end this recursion
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition recursively
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i = i+1     # increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i] # swap the location of smaller and larger value

    arr[i+1], arr[high] = arr[high], arr[i+1] # swap the pivot with the first higher number
    return (i+1)

# Implement quickSort
arr = [10, 7, 8, 9, 1, 5]
low, high = 0, len(arr) - 1
quickSort(arr, low, high)
