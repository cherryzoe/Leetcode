给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

解题思路：

维护正最大和负最小的数组，dp[i]指考虑当前nums[i]的最大和最小结果

遍历一遍数组，每个元素有两种情况：
1. 加入前面的累计乘积 dp[i-1] * nums[i]
2. 以当前元素为起点重新开一个 

因为有负数出现，如果当前元素是负数，那么取前面的负最小值与之相乘得到最大值

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dpmax = [1 for _ in range(len(nums))]
        dpmin = [1 for _ in range(len(nums))]
        res = -sys.maxsize

        dpmax[0] = dpmin[0] = nums[0]

        for i in range(1, len(nums)):
            dpmax[i] = max(dpmax[i-1] * nums[i], nums[i], dpmin[i-1] * nums[i])
            dpmin[i] = min(dpmin[i-1] * nums[i], nums[i], dpmax[i-1] * nums[i])
            
        return max(dpmax)

 class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dpmax = dpmin = nums[0]
        res = -sys.maxsize

        for i in range(1, len(nums)):

            if nums[i] < 0:
                dpmax, dpmin = dpmin, dpmax

            dpmax = max(dpmax * nums[i], nums[i])
            dpmin = min(dpmin * nums[i], nums[i])
            res = max(res, dpmax)
        return res
