# Given a sorted integer array without duplicates, return the summary of its ranges.

# Example 1:

# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# Example 2:

# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

# 只需遍历一遍数组即可，每次检查下一个数是不是递增的，如果是，则继续往下遍历，如果不是了，我们还要判断此时是一个数还是一个序列，
# 一个数直接存入结果，序列的话要存入首尾数字和箭头“->"。
# 我们需要两个变量start和end，end == start，说明只有一个数字，若 end > start，则是一个连续序列

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        start = end = 0
        r = ''
        while end < len(nums):
            if end + 1 < len(nums) and nums[end+1] - nums[end] == 1:
                end += 1
            else:
                if end > start:
                    r = str(nums[start]) + '->' + str(nums[end])
                   
                else:
                    r = str(nums[start])
                res.append(r)
                start = end + 1
                end = start
        return res
                
            
        
