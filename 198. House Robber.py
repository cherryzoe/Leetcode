# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

# 解题思路：
# 对于第n户人家， 有两种选择： 抢或者不抢。 
# a.） 如果抢：因为中间至少要隔一家， 第i-1户人家一定不可以抢， dp[i-2] 到第i-2户人家时候的累积金钱数量 + nums[i]（第i户人家的金钱数） 
# b.） 不抢， 那么第i-1家则可以抢， dp[i-1]是到第i-1户人家时候的累积金钱数量

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]
        
        dp = [0 for i in range(size)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max ( dp[i-2] + nums[i] , dp[i-1] )
            
        return dp[size - 1]

   
