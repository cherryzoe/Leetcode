# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

# Example 1:
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
# Note:
# 1 <= k <= n <= 30,000.
# Elements of the given array will be in the range [-10,000, 10,000].



# ===solution1: brute force ==> timeout==
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        if len(nums) == k:
            return sum(nums)/float(k)
        else:
            lst = []
            for i in range(0, len(nums)-k+1):
                lst.append(sum(nums[i:i+k]))
            return float(max(lst))/k
        
   

# ===solution 2: slide window ===
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sub_sum = sum(nums[i] for i in range(k))
        sub_max = sub_sum
        for i in range(k, len(nums)):
            sub_sum += nums[i] - nums[i-k]
            sub_max = max(sub_sum, sub_max)
        return float(sub_max)/k
