Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? 

(The output array does not count as extra space for the purpose of space complexity analysis.)
我们以一个4个元素的数组为例，nums=[a1,a2,a3,a4]，要想在O(n)的时间内输出结果，比较好的解决方法是提前构造好两个数组：
[1, a1, a1*a2, a1*a2*a3]
[a2*a3*a4, a3*a4, a4, 1]
然后两个数组一一对应相乘，即可得到最终结果 [a2*a3*a4, a1*a3*a4, a1*a2*a4, a1*a2*a3]。
不过，上述方法的空间复杂度为O(n)，可以进一步优化成常数空间，即用一个整数代替第二个数组。

Solution1: O(n) space
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [1] * n
        right = [1] * n
        res = [1] * n
        
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        for j in range(n-2, -1, -1):           
            right[j] = right[j+1] * nums[j+1]
        for t in range(n):
            res[t] = left[t] * right[t]
        return res
        
Solution2 O(1) space
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [1] * n
        
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
            
        right = 1
        for j in range(n-1, -1, -1):
            left[j] *= right
            right *= nums[j]
            
        return left

        
  
