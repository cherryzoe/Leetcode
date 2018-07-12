A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
             
Solution 1 Sequence search:             
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return i-1
        return len(nums)-1  
        
        
 Solution 2 Binary search(iteration)
 class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums)-1
        while lo < hi:
            m1 = lo + (hi - lo)/2
            m2 = m1 + 1
            if nums[m1] > nums[m2]:
                hi = m1
            else:
                lo = m2
        return lo
 
 Solution3 Binary Search(recursive)
 class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, 0, len(nums)-1)
        
    def helper(self, nums, lo, hi):
        
        if lo == hi:
            return lo
        else:
            m1 = lo + (hi - lo)/2
            m2 = m1 + 1
            if nums[m1] > nums[m2]:
                return self.helper(nums, lo, m1)
            else:
                return self.helper(nums, m2, hi)   
   
 
