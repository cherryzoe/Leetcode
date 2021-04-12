You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.
A number x is considered missing if x is in the range [lower, upper] and x is not in nums.
Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.
Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

Example 1:

Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: ["2","4->49","51->74","76->99"]
Explanation: The ranges are:
[2,2] --> "2"
[4,49] --> "4->49"
[51,74] --> "51->74"
[76,99] --> "76->99"
Example 2:

Input: nums = [], lower = 1, upper = 1
Output: ["1"]
Explanation: The only missing range is [1,1], which becomes "1".

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):

        res = []
        low = lower
        for i in range(len(nums)):
            if nums[i] == low:
                low += 1
            else:
                if nums[i]- 1 > low:
                    res.append(str(low) + '->' + str(nums[i]-1))
                elif nums[i] - 1 == low: 
                    res.append(str(low))
                low = nums[i] + 1
       
        # Note that we when low > upper here we should not append anything into result. and that's why we don't use if-else here
        if low < upper:
            res.append(str(low) + '->' + str(upper))
        if low == upper:
            res.append(str(low))
        return res 


    

