# Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

# Example 1:
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
# Example 2:
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]
# Note:
# The value k is positive and will always be smaller than the length of the sorted array.
# Length of the given array is positive and will not exceed 104
# Absolute value of elements in the array and x will not exceed 104

# 解题思路：二分是找出x的位置，然后找出其旁边的k个数

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if not arr:
            return -1
        
        lo, hi = 0, len(arr) - 1
        while lo + 1 < hi:
            mid = lo + (hi-lo)/2
            if arr[mid] > x:
                hi = mid
            else:
                lo = mid
        if arr[lo] > x:
            return arr[:k]
        if arr[hi] < x:
            return arr[-k:]
        
        res = []
        left, right = lo, hi
        while len(res) < k:
            if left < 0:
                res.append(arr[right])
                right += 1
            elif right >= len(arr):
                res.append(arr[left])
                left -= 1
            else:
                if x - arr[left] > arr[right] - x:
                    res.append(arr[right])
                    right += 1
                else:
                    res.append(arr[left])
                    left -= 1
        return sorted(res)
        
