Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = [0]
        if nums.count(1) == 0:
            return 0
        else:
            for idx, item in enumerate(nums,1):
                if item == 0:
                    index.append(idx)
            index.append(len(nums) +1)
            return max([j-i-1 for i,j in zip(index[:-1], index[1:])])
