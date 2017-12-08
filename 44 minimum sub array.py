Lintcode 44

Given an array of integers, find the subarray with smallest sum.
Return the sum of the subarray.
Notice: The subarray should contain one integer at least.

class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        mini = summ = nums[0]
        for i in nums[1:]:
            if i+summ < i:
                summ += i
            else:
                summ = i
            mini = min(summ, mini)
        return mini
