# Rotate an array of n elements to the right by k steps.

# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

#solution 3:
# Original List                   : 1 2 3 4 5 6 7
# After reversing all numbers     : 7 6 5 4 3 2 1
# After reversing first k numbers : 5 6 7 4 3 2 1
# After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
# https://leetcode.com/articles/rotate-array/ 
# other reverse functions: https://www.quora.com/How-can-I-reverse-a-list-in-python

# Note: 
#     1. reverse() parameter end should always less than n-1, otherwise index will out of range
#     2. k could be greater than n, so k%n => k. (a number rotate n time would come back to the original place.)
#     3. use start,end for reverse is much better than index, 1/2 length. 

    class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        n = len(nums)
        k %= n
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)
    
    


# solution 1: (correct result run in local but incorrect with online judge) why?
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        lst = []
        for i in range(n-k, n):
            lst.append(nums[i])
        for i in range(n-k):
            lst.append(nums[i])
        nums = lst
        
# wrong answer:
# [1,2]
# 1
# Output:
# [1,2]
# Expected:
# [2,1]        

#solution2(wrong answer) - wrong case - input [1,2] k=3
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lst = []
        n = len(nums)
        if n < 2:
            return nums
        else:
            for i in range(n-k, n):
                lst.append(nums[i])
            for i in reversed(range(k,n)):
                nums[i] = nums[i-k]
            for i in range(k):
                nums[i] = lst[i]
