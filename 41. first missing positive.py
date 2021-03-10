Given an unsorted integer array nums, find the smallest missing positive integer.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
 

Constraints:

0 <= nums.length <= 300
-231 <= nums[i] <= 231 - 1

解题思路：
用cyclic sort,把给定输入数组长度范围内的index排上对应的数字。
遍历排序之后的数组，第一个含非正确数字的位置就是我们要找的。注意+1和-1
如果遍历完数组依旧未找到，那么就是数组长度+1的数。

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        while cur < len(nums):
            nex = nums[cur] - 1
            if nex >= 0 and nex < len(nums) and nums[nex] != nums[cur]:
                nums[nex], nums[cur] = nums[cur], nums[nex]
            else: 
                cur += 1

        for i in range(len(nums)):
            if i != nums[i] - 1:
                return i + 1
        return len(nums) + 1
