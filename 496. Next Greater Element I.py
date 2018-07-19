You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.

#use dictionary to store the position-value of nums so that we can find the position faster
我们用哈希表先来建立每个数字和其坐标位置之间的映射，那么我们在遍历子集合中的数字时，就能直接定位到该数字在原数组中的位置，然后再往右边遍历寻找较大数即可
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(findNums)
        dic = {v:i for i,v in enumerate(nums)}
        for n in range(len(findNums)):
            start = dic[findNums[n]] + 1
            for i in range(start, len(nums)):
                if nums[i] > findNums[n]:
                    res[n] = (nums[i])
                    break
            
        return res
                
Bruce force:
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        res = []
        for n in findNums:
            for j in range(len(nums)):
                if n == nums[j]:
                    break
            i = j + 1
            while i < size and nums[i] < n:
                i += 1
            if i < size:
                res.append(nums[i])
            else:
                res.append(-1)
        return res
            
