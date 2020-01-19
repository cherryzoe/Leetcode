# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.

# Example:

# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Follow up:

# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?
Note: 
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p,l,r = 0, 0, len(nums)-1
#         L往左的所有数应都已被换成0， R往右的数都是2
        while p <= r:
            if nums[p] == 0:
                nums[p], nums[l] = nums[l], nums[p]
                p += 1
                l += 1     #当P与l交换后，无需在此判断p指向的数，因为p已经做过l的位置，显然知道换过来的数必然是1
            elif nums[p] == 2:
                nums[p], nums[r] = nums[r], nums[p]
                r -= 1     #而当P与R交换后，R原本对应的数我们并不知道会是多少，所以换到P位置后，P不能直接移动到下一位，需要再次判断P位置上的数
            else:
                p += 1
        return nums
