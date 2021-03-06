Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start + (end - start)/2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid -1
                else:
                    start = mid + 1
                print 'left half', start, end, mid
            if nums[mid] < nums[end]:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid -1
                print 'right half', start, end, mid
        return -1


#wrong solution: need to figure out why it's not working below: 
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        x = 1
     
        def binarySearch(self, l, r, target):
            while l <= r:
                mid = l + (r-l)/2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid -1
                else:
                    l = mid + 1
        return -1
    
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                x = i
                break
        if target >= nums[0]:
            binarySearch(0, x-1, target)
        else:
            binarySearch(x, len(nums)-1, target)
