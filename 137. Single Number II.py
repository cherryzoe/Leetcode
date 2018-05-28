Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

Solution2: correct without extra memory
idea: 
    ones: capture numbers occur once
    twos: capture numbers occur twice
  
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = twos = 0
        for n in nums:
            ones = (ones ^ n) & ~twos
            twos = (twos ^ n) & ~ones
        return ones


Solution 1: with extra memory, Not acceptable
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = collections.Counter(nums)
        for i,v in dic.items():
            if v == 1:
                return i
