# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

class Solution(object):
    def searchRange(self, nums, target):     

        l,r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)/2
            #继续找左边界
            if nums[m] == target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        if l >= len(nums) or nums[l] != target:
            return [-1, -1]
        else:
            start = l

        l,r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)/2
            #继续找右边界
            if nums[m] == target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        end = r 
        return [start, end]

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        return [self.findLeft(nums, target), self.findRight(nums, target)]
        
    def findRight(self, nums, target):
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = (end + start)/2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start  
        else:
            return -1
        
    def findLeft(self, nums, target):
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = (end + start)/2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        else:
            return -1
