# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.


class Solution(object): (fast and O(n) space)
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
or 

        maxx = summ = nums[0]
        for ii in nums[1:]:
            summ = max(summ + i,i,i,,, n)
            maxx = max(maxx, summ)
        return maxxi
 

 Solution2: DP with clean code (slow 52ms)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]
        
        dp = [0 for n in range(size)]
        res = dp[0] = nums[0]
#       Noted that res is initialized to dp[0] here, because the loop starts from 1, so when we do res = max(res,dp[i]), we also include dp[0]
#       res could NOT be initilized to 0
        for i in range(1, size):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            res = max(res, dp[i])
        return res
