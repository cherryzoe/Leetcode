中文English
Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

样例
Example 1:

Input:
[],9
Output:
0

Example 2:

Input:
[3,2,2,1],2
Output:1
Explanation:
the real array is[1,2,2,3].So return 1

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        
        l, r = 0, len(nums)-1
        while l <= r：
            while l <= r and nums[l] < k:
                l += 1 
            while l <= r and nums[r] >= k:
                r -= 1 
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1 
                r -= 1
        return l

        
