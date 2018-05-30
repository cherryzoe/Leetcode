# Given an array of integers, find two non-overlapping subarrays which have the largest sum.
# The number in each subarray should be contiguous.
# Return the largest sum.

# 这一题有点像buy stock III, 分割两边然后再求最大值的做法，所以采取类似的做法
# 如果采取maximum subarray的办法去求每一个index的两边，则需要 O(n^2)
# 这里才去和buy stock III类似的题目，但是略有不同 对于左边，用两个array left[]和leftMax[] left[i]表示以i为end的subarray的maximum sum leftMax[i]表示在[0:i]区间内的subarray的maximum sum （不一定以nums[i]为end）
# 右边同理，剩下的同buy stock iii

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
#         初始化数组时不能用 left = right = array[]， 这样会将left 和 right 指向同一个数组的起始地址，错误！不要问我怎么知道的
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
