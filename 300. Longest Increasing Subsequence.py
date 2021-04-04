Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """  
        # 新建数组 cell，用于保存最长上升子序列。
        # 对原序列进行遍历，将每位元素二分插入 cell 中。
        # 如果 cell 中元素都比它小，将它插到最后
        # 否则，用它覆盖掉比它大的元素中最小的那个。
        # 总之，思想就是让 cell 中存储比较小的元素。这样，cell 未必是真实的最长上升子序列，但长度是对的。
        cell = [nums[0]]
        for n in nums[1:]:
            if n > cell[-1]:
                cell.append(n)

            l, r = 0, len(cell)-1
            while l < r:
                m = l + (r-l)/2
                if cell[m] < n:
                    l = m + 1
                else:
                    r = m           
            cell[l] = n 
        return len(cell)

# 解法2： 时间复杂度 n * n
      res = 1 # [7,7,7,7]这种case的输出是1。此外如果给定的数组中没有一个单调递增的子序列，此时也是返回1，某个元素单独成列
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
          if nums[j] < nums[i]:
              dp[i] = max(dp[i], dp[j]+1)
              res = max(res, dp[i])
  return res 
        
