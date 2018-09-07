
# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

# Example 1:

# Input: 11
# Output: 3
# Explanation: Integer 11 has binary representation 00000000000000000000000000001011 
# Example 2:

# Input: 128
# Output: 1
# Explanation: Integer 128 has binary representation 00000000000000000000000010000000

Solution 1: Bit shifting
class Solution(object):
def hammingWeight(self, n):
    """
    :type n: int
    :rtype: int
    """
    res = 0
    while n:
        res += n & 1
        n = n >> 1
    return res

Solution2: Bit manipulate to clear the least bit    
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n:
            n = n & (n-1) 
#convert the rightmost bit of 1 into 0 for each loop. until all 1s are turned into 0(n==0)
            cnt += 1
        return cnt
