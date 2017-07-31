Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.


solution 1: (correct result run in local but incorrect with online judge)
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        lst = []
        for i in range(n-k, n):
            lst.append(nums[i])
        for i in range(n-k):
            lst.append(nums[i])
        nums = lst
        
wrong answer:
[1,2]
1
Output:
[1,2]
Expected:
[2,1]        
