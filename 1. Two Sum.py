# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
 

 1/17/2020
 class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dic = {value: idx for idx, value in enumerate(nums)}
        
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in dic and dic[temp] != i:
                return [i, dic[temp]]
        return False
 
 
 def twoSum(self, numbers, target):
        # write your code here
        if len(numbers) < 2:
            return False
        dic = {}
        for i in range(len(numbers)):
            if numbers[i] in dic:
                return [dic[numbers[i]], i]
            else:
                dic[target - numbers[i]] = i
        
