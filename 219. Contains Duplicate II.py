# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.



# solution1: (brute force - time out as result)
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j] and j-i <= k:
            return True
return False



# solution 2: (use dic to store history data)
# note: use single character for index and value in dictinary to avoid typo
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i,v in enumerate(nums):
            if v in dic and i-dic[v] <= k:
                return True
            dic[v] = i
        return False
