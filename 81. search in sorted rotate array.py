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
此时接着判断target落在哪个区间，左区间单调递增，右区无序，所以我们只要检查是否满足left <= target < mid的条件,满足的话就是在有序的左区间，不满足就只能在右边。 
左边单调递增，最大值在mid, 如果target比mid还要大，那只可能在右区间。因此移动left 或者 right缩小范围继续寻找
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
