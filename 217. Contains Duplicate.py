# Given an array of integers, find if the array contains any duplicates. 
# Your function should return true if any value appears at least twice in the array, 
# and it should return false if every element is distinct.


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if len(nums) < 2:
            return False
        else:
            return len(nums) != len(set(nums))
        
 solution2:
       s = set()
       for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False

 solution3:
#     思路：先排序然后判断相邻是否重复
