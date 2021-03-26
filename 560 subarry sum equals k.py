Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
此题一开始想到用滑动窗口，可是因为输入数组中存在负数，因此会出现窗口不断拓展但是总值减小的情况。所以还是用前缀和加hash map。

解法一：【最优解】
用字典记录前缀和出现的次数 时间复杂度：O（N） 

  class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        presum = 0
        dic = {}
        cnt = 0

        for i in range(len(nums)):
            presum += nums[i]
            #当前前缀和就是K
            if presum == k:
                cnt += 1
            #可以与之前的前缀和相减得到K
            if presum - k in dic:
                cnt += dic[presum-k]
            #结束判断后，再把当前的presum加入字典，否则 presum-k == presum 的这种情况就会重复判断到自己
            if presum not in dic:
                dic[presum] = 1
            else:
                dic[presum] += 1
        return cnt 

解法二：前缀和解法：双重循环求前缀和，暴力遍历所有可能解，时间复杂度 O(N2)
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        le = len(nums)
        cnt = 0
        presum = [0] * (le+1)
        
        for i in range(le):
            presum[i+1] = nums[i] + presum[i]
            

        for i in range(le):
            for j in range(i, le):
                if presum[j+1] - presum[i] == k:
                    cnt += 1
        return cnt
