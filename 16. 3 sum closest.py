Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

解题思路： 先排序后用双指针

固定第一个元素，用双指针在后面缩小区间查找，不断检测当前的差值，并维护一个最小差值变量，当前是最小差值时，同时记录当前的和
  
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums = sorted(nums)
        min_diff = sys.maxsize
        res = 0

        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            
            while left < right:
                diff = target - nums[i] - nums[left] - nums[right]
                if diff == 0:
                    return target

                if abs(diff) < min_diff:
                    min_diff = abs(diff)
                    res = target - diff

                if diff < 0:
                    right -= 1
                else:
                    left += 1
        return  res
