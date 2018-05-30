Given an array of integers, find two non-overlapping subarrays which have the largest sum.
The number in each subarray should be contiguous.
Return the largest sum.

import sys
class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        maxSum = -sys.maxint
        size = len(nums)
        maxLeft = [0]*size
        maxRight = [0]*size
        left = [0]*size
        right = [0]*size
        
        left[0] = maxLeft[0] = nums[0]
        for i in range(1, size):
            left[i] = max(left[i-1]+nums[i], nums[i])
            maxLeft[i] = max(left[i], maxLeft[i-1])
            
        right[-1] = maxRight[-1] = nums[-1]
        for i in range(size-2, -1, -1):
            right[i] = max(nums[i], right[i+1]+nums[i])
            maxRight[i] = max(right[i], maxRight[i+1])

        for i in range(size-1):
            curSum = maxLeft[i] + maxRight[i+1]
            maxSum = max(maxSum,curSum)
        return maxSum
