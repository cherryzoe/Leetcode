Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.



class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF
        MASK = 0x100000000
        
        if a == 0:
            return b
        if b == 0:
            return a
        
        while b != 0:
            _sum = (a ^ b)  % MASK //calculate sum of a and b without thinking the carry 
            b = ((a & b)<<1) % MASK //calculate the carry
            a = _sum //add sum(without carry) and carry
        return a if a <= MAX_INT else ~((a & MAX_INT) ^ MAX_INT)
