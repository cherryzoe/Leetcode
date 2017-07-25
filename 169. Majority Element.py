
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.



# Note:
# algorithm refernce:
# http://www.cs.utexas.edu/~moore/best-ideas/mjrty/example.html#step13

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use count to store the value, set the major count(default is nums[0]) to 1
        # loop through the list, if got a different value, count--
        # when count is 0, set the current value as the major
        
        major = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if count == 0:
                major = nums[i]
                count += 1
            elif nums[i] == major:
                count += 1
            else:
                count -= 1
        return major
            