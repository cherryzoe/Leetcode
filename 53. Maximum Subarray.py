# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxx = nums[0]
        summ = nums[0]
# i is from the second element for case like the input only has one element such as [1]
        for i in nums[1:]:
            if i+summ > i:
                summ += i
            else:
                summ = i
            maxx = max(summ, maxx)
        return maxx
