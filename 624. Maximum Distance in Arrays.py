# Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

# Example 1:
# Input: 
# [[1,2,3],
#  [4,5],
#  [1,2,3]]
# Output: 4
# Explanation: 
# One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
# Note:
# Each given array will have at least 1 number. There will be at least two non-empty arrays.
# The total number of the integers in all the m arrays will be in the range of [2, 10000].
# The integers in the m arrays will be in the range of [-10000, 10000].

#Full explaination of the algorithm - Leetcode Article
class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        left = arrays[0][0]
        right = arrays[0][-1]
        res = 0
        for n in arrays[1:]:
            res = max(res, abs(n[-1]-left), abs(right - n[0]))
            left = min(left, n[0])
            right = max(right, n[-1])
        return res    
