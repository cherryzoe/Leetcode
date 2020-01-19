iven an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2 
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        k = len(nums) - 1
        cnt = 0
        
        while k > 1:
            l, r = 0, k-1
            while l < r:
                if nums[l] + nums[r] < target - nums[k]:
                    cnt += r - l
                    l += 1
                else:
                    r -= 1
            k -= 1
        return cnt
                
