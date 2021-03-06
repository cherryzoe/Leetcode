# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place and use only constant extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

# refernce:
# http://www.cnblogs.com/grandyang/p/4428207.html
# 1. 首先从右向左遍历数组，找到第一个相邻的左<右的数对，记右下标为x，则左下标为x - 1
# 2. 若x > 0，则再次从右向左遍历数组，直到找到第一个大于nums[x - 1]的数字为止，记其下标为y，交换nums[x - 1], nums[y]
# 3. 最后将nums[x]及其右边的元素就地逆置

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        le = len(nums)
        i = le - 1

        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        if i <= 0:
            nums.reverse()
            return
        else:
            j = i
            while j < le and nums[j] > nums[i-1]:
                j += 1
            nums[i-1], nums[j-1] = nums[j-1], nums[i-1]
            nums[i:] = nums[i:][::-1]


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        for x in range(size-1, -1, -1):
            if nums[x-1] < nums[x]:
                break
        if x:
            # 第一次出错因为没有判断x是否大于0，输入【3.2.1】，第一个循环结束时得到的 x = 0, 其实是没有找到合适的值，循环结束。 结果也错误
            for y in range(size - 1, x-1, -1):
                if nums[y] > nums[x-1]:
                    nums[y], nums[x-1] = nums[x-1], nums[y]
                    break
                
        l,r = x, size-1
        
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
