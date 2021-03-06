# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# For example,
# Given input array nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

# consider corner case, expecially when the input = []. 
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        else:
            index = 0
            for i in nums[1:]:
                if i != nums[index]:
                    index += 1
                    nums[index] = i
            return index+1

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        idx = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[idx]:
                idx += 1
                nums[idx] = nums[i]
        return idx+1                
                
            