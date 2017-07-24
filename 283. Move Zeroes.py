Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # two pointer:
        # 1. use index to point to the position of 0
        # 2. use another loop to go through the list, 
        # if the number is non-zero, copy it into index position.
        # after whole list done, replace the rest of the list into zero

        index = 0
        for n in nums:
            if n != 0:
                nums[index] = n
                index += 1
        for i in range(index, len(nums)):
            nums[i] = 0
        print nums
