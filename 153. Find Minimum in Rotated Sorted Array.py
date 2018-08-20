# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# You may assume no duplicate exists in the array.

# Example 1:

# Input: [3,4,5,1,2] 
# Output: 1
# Example 2:

# Input: [4,5,6,7,0,1,2]
# Output: 0

# 解题思路：
# 本题可以从头至尾遍历得到最小元素，但是时间复杂度O(n)
# 利用二分搜索可以降低至O（lgn)。 旋转后的数组可以划分为两个排序的子数组，前面的子数组元素都大于或等于后面的数组元素。 最小元素刚好是这两个子数组的边界。
# 中间元素如果位于前面递增子数组，那么应该大于等于第一个指针指向的元素，此时最小元素位于该中间元素后面，我们把第一个指针向该中间元素移动以缩小寻找范围。
# 同样，如果中间元素位于后面的递增子数组，那么它应该小于或等于hi指针指向的元素。此时最小元素位于mid左边。将hi移动到mid位置，缩小寻找范围。
# 按照以上思路， lo总是指向前面递增数组（当lo与hi重合时即越过边界， 到达最小元素），hi总是指向后面递增数组。

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        
        if not size:
            return None
        
        lo, hi = 0, size-1  
        
        while hi > lo:
            if nums[hi] > nums[lo]:
                return nums[lo]
            
            mid = lo + (hi - lo)/2
            
            if nums[mid] >= nums[lo]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]
    
    
