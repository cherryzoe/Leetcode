Description
Given an array with integers.

Find two non-overlapping subarrays A and B, which |SUM(A) - SUM(B)| is the largest.

Return the largest difference.

The subarray should contain at least one number

Have you met this question in a real interview?  
Example
For [1, 2, -3, 1], return 6.

Challenge
O(n) time and O(n) space.



class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """
    def maxDiffSubArrays(self, nums):
        # write your code here
        size = len(nums)

        left_min = [0 for x in range(size)]
        right_min = [0 for x in range(size)]
        left_max = [0 for x in range(size)]
        right_max = [0 for x in range(size)]
        
        min_sum = max_sum = left_max[0] = left_min[0] = nums[0]
        for i in range(1, size):
            cur = nums[i]
            min_sum = min(min_sum + cur, cur)
            max_sum = max(max_sum + cur, cur)
            left_min[i] = min(left_min[i-1], min_sum)
            left_max[i] = max(left_max[i-1], max_sum)
        # print left_max, left_min
        
        min_sum = max_sum  = right_max[size-1] = right_min[size-1] = nums[-1]
        for i in range(size-2, -1, -1):
            cur = nums[i]
            min_sum = min(min_sum + cur, cur)
            max_sum = max(max_sum + cur, cur)
            right_min[i] = min(right_min[i+1], min_sum)
            right_max[i] = max(right_max[i+1], max_sum)
        # print right_min, right_max
        
        diff = 0
        for i in range(size-1):
            diff = max(diff,abs(left_min[i] - right_max[i+1]))
            diff = max(diff, abs(left_max[i] - right_min[i+1]))
        return diff
