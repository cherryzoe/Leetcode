Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        //assume that the different int are A and B
        res = [0,0]
        AxorB = 0
        for n in nums:
            AxorB ^= n
        //get the most right bit that is different between A and B. 
        flag = ~(AxorB - 1) & AxorB
        for n in nums:
        //Get back to the array find the ones have 1 in the same bit, xor all of them. 
        //all pairs will become 0 after xor and the single one will left
            if n & flag == 0:
                res[0] ^= n
            else:
                res[1] ^= n
        return res
        
