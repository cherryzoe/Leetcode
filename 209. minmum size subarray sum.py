给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。


示例：

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
 

进阶：

如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

1. 滑动窗口 时间复杂度O(n)
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = sys.maxsize
        i, j = 0, 0
        temp = 0
        while j < len(nums):
            temp += nums[j]
            while temp >= s:
                res =min(res, j-i+1)
                temp -= nums[i]
                i += 1
            j += 1
        if res == sys.maxsize:
            return 0 
        return res
