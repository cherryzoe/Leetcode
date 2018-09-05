Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

solution 1: Set() fastest
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)
        
# use dictionary will be fast two!!!
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        dic = {}
        for i in nums1:
            dic[i] = True
        for i in nums2:
            if i in dic:
                dic[i] = False
        for i,v in dic.items():
            if v == False:
                res.append(i)
        return res
        
        
solution 2: list a little bit slower than set in python
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = set()
        for i in nums1:
            if i in nums2:
                res.add(i)
                nums2.remove(i)
        return list(res)
        
solution 3: binary search slowest
class Solution(object):
    
    def binarySearch(self, target, nums):
        nums = sorted(nums)
        l, r = 0, len(nums)

        while l < r:
            m = l + (r-l)/2
            if nums[m] == target:
                return True
            elif nums[m] < target:
                l = m + 1
            else:
                r = m
        return False
    
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = set()
        for i in nums2:
            if self.binarySearch(i, nums1):
                res.add(i)
        return list(res)
        
    
        
