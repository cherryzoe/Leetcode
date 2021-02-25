our are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        product = 1
        cnt = 0
        start = 0

        for end in range(len(nums)):
            product *= nums[end]

            while start < len(nums)-1 and product >= k:
                product /= nums[start]
                start += 1
            # 此时，以right为右边界，以滑动区间中任一元素为左边界的子数组都满足题意
            # 由此可以得到以right为子数组右边界的所有子树组的个数right-left+1
            cnt += end - start + 1
            
        return cnt 

