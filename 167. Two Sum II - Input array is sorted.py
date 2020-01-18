# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution and you may not use the same element twice.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

1/18/2020
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers)-1
        
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l+1, r+1]
            if sum > target:
                r -= 1
            else:
                l += 1
        return False

Solution1:
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # usd dictionary to record scaned data, when return, return the index from dictionay first as index1, which is always               smaller than index2. 
        dic = {} 
        for idx, num in enumerate(numbers,1):
             if target-num in dic:
                return [dic[target-num],idx]
             dic[num] = idx

Solution2: Using two pointer from start and end of array
        
