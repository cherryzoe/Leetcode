Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if not size:
            return
        
        lo, hi = 0, size-1
        
        while lo < hi:
            if nums[hi] > nums[lo]:
                return nums[lo]
            
            mid = lo + (hi-lo)/2
            
            if nums[mid] == nums[lo] == nums[hi]:
                return self.linearSearch(nums, lo, hi)
            
            if nums[mid] >= nums[lo]:
                lo = mid + 1
            elif nums[mid] <= nums[hi]:
                hi = mid
        return nums[lo]
    
    def linearSearch(self, nums, start, end):
        res = nums[start]
        for i in range(start, end+1):
            if nums[i] < res:
                res = nums[i]
        return res
        
            
                
        
