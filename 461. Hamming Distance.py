# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.

# Example:
# Input: x = 1, y = 4
# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ?   ?

# The above arrows point to positions where the corresponding bits are different.

# solution1: 
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')
        
        
# Solution 2: Brian Kernighan's bit counting algorithm
    
class Solution(object):
def hammingDistance(self, x, y):
         n = x ^ y
        cnt = 0
        while n:
            cnt += 1
            n &= n-1 # convert the most right 1 into 0 in n
        return cnt

