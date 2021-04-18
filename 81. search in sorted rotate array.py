假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false

解题思路：

二分搜索法，

取mid 与left比较，
如果 mid > left,说明左半边是单调递增的，最小值是left，最大值是mid，旋转点在右半边。
此时接着判断target落在哪个区间，左区间单调递增，右区无序，所以我们只要检查是否满足left <= target < mid的条件,满足的话就是在有序的左区间[:mid]，不满足就只能在右边[mid:]。 
左边单调递增，最大值在mid, 如果target比mid还要大，那只可能在【mid:]右区间。因此移动left 或者 right缩小范围继续寻找
判断target的等号取在left 或者 right上面，而不是mid,因为mid 的值总归都会在循环一开始检查是否等于target。

如果mid < left, 说明右半边是单调递增，最小值是mid，最大值是right,旋转点在左边，左边无序。
此时接着判断target落在哪个区间，如果target比右区的最大值还要大或比最小值还要小，说明target肯定不在右边有序递增的区间里面，一定在左边，此时移动right = mid-1，缩小范围进一步搜索

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left)/2

            if nums[mid] == target:
                return True

            if nums[mid] == nums[left]:
                left += 1

            elif nums[mid] > nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

#  Better solution 
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        # 1. find the roation point 
        rt = 0
        l, r = 0, len(nums)-1
        # 去除重复，并且重新定义nums数组 - 很关键
        while l < r and nums[0] == nums[r]:
            r -= 1
        nums = nums[:r+1]

        # 找出转折点rt - 左半边递增区间最后一个值
        while l <= r:
            m = l +(r-l)/2
            if nums[m] == target:
                return True
            if m < len(nums)-1 and nums[m] >= nums[0] and nums[m] > nums[m+1]:
                rt = m
                break
            if nums[m] >= nums[0]:
                l = m + 1
            else:
                r = m -1
        # 2. 判断是否有转折 - 如果有转折点，上面while循环出来的时候l,r应该没有交叉。当遍历完所有节点未发现转折点，
        # 出循环的时候l,r一定是相交叉的
        if l > r:
            l,r = 0, len(nums)-1
        else:
            # 判断target在转折点前或者后,去相应的单调区间查找
            if target == nums[0]:
                return True
            # 重新分配l, r的起始位置，万不可以偷懒继承之前的位置，出错点
            elif target > nums[0]:
                l, r = 0, rt
            else:
                l, r = rt+1, len(nums)-1
        # 3. 相应区间查找
        while l <= r:
            m = l + (r-l)/2
            if nums[m] == target:
                return True
            if nums[m] > target:
                r = m -1
            else:
                l = m + 1
        return False
