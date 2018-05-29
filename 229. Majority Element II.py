Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]

Solution： Boyer Moore majority vote algorithm
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return [] //此处返回【】 而非 None， 因为题目要求返回数组
        m1 = nums[0]
        m2 = None
        c1 = 1
        c2 = 0
        for n in nums[1:]:
            # in case of [2,2]
            if n == m1:
                c1 += 1
            elif n == m2:
                c2 += 1
            elif c1 == 0:
                c1, m1 = 1, n  # c1 should be set to 1 for the first m1
            elif c2 == 0:
                c2, m2 = 1, n
            else:
                c1 -= 1
                c2 -= 1
        return [n for n in (m1, m2) if nums.count(n) > len(nums)/3]
