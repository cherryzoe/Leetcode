# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1. 

# Idea: iterate throught the list, compare two continous element, use variable cnt record if it's increasing. otherwise reset cnt to 1.

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        cnt = 1
        size = len(nums)
        
        if size == 0:
            return 0
        
        if size  ==  1:
            return 1

        for i in range(1, size):
            if nums[i] > nums[i-1]:
                cnt += 1
            else:
                cnt = 1
            res = max(res, cnt)
        return res
