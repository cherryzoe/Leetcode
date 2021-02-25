给定一个二进制数组，你可以最多将 1 个 0 翻转为 1，找出其中最大连续 1 的个数。

示例 1：

输入：[1,0,1,1,0]
输出：4
解释：翻转第一个 0 可以得到最长的连续 1。
     当翻转以后，最大连续 1 的个数为 4。

 解题思路：滑动窗口 - 维护一个最多有一个0的滑动窗口，当窗口中0的个数大于1时，开始缩小左边直到窗口只剩下一个0为止
  
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = 0
        start = 0
        cnt = 0 

        for end in range(len(nums)):
            if nums[end] == 0:
                cnt += 1
            end += 1
            
            while cnt > 1:
                if nums[start] == 0:
                    cnt -= 1
                start += 1           
           # 右边界每增加1位，当前长度都会被记录
            res = max(res, end-start)

        return res


