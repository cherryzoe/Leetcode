# Given an array of integers, every element appears twice except for one. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Solution 1: Bit computation (fast and no extra space)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res ^=  i  # after XOR: A xor A  = 0, 0 xor B = B => single number 
        return res



Solution 2: (slow and need extra space)
    Use dictionary record occurance of each element and return the occurence == 1
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        
        for i in nums:
            dic[i] = dic.get(i, 0) + 1  #get the value of key == i, if i is not exist, then return 0
        
        for key, val in dic.items(): # Dic.items() return key and val together
            if val == 1:
                return key
