给定一个增序排列数组 nums ，你需要在 原地 删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1：

输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 你不需要考虑数组中超出新长度后面的元素。

cur-1 cur  i
1      1   1  2 2 3
解题思路：
原地替换用双指针，cur指向写入位置，i遍历一遍数组。不断比较nums[i]与nums[cur-1]，若不相等，则在cur+1位置写入nums[i]的值。
cur 与 cur+1 有两种情况：相等或者不等。
N[cur-1] == N[cur] - > N[i] == N[cur-1] -> N[i]将是第三个重复的数字，因此不能被写入 
                       N[i] != N[cur-1] -> N[i]可以被写入，此是N[i]与N[cur],N[cur+1]均不相等
N[cur-1] != N[cur] - > N[i]不论如何都不可能等于N[cur-1]，因为数组递增。N[i]有可能等于N[cur]但是不影响结果。

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        cur = 1
        for i in range(2, len(nums)):
            if nums[i] != nums[cur - 1]:
                cur += 1
                nums[cur] = nums[i]
        return cur + 1
