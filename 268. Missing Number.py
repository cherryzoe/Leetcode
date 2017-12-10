# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# For example,
# Given nums = [0, 1, 3] return 2.

# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

# be careful that return type is int not set or list

upate on 12/10/2017

solution 2:
 def missingNumber(self, nums):
    return reduce(operator.xor, nums + range(len(nums)+1))

solution 3:（faster than sol 2)
    def missingNumber(self, nums):
        n = len(nums)
        return n*(n+1)/2 - sum(nums)

solution 1:
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A = {i for i in range(len(nums)+1)}
        B = set(nums)
        for i in A.difference(B):
            return i
