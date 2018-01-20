Implement pow(x, n).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Idea:
- if n = 0: return 1
- if n < 0: return 1/(x, -n)
- if n = odd: x^n = (x ^ n/2)*(x ^ n/2) *x   eg: 2^7 = (2 ^ 3) * (2 ^ 3) * 2
- if n = even x^n = (x ^ n/2)*(x ^ n/2)      eg:5^6 = (5 ^ 3) * (5 ^ 3) 

lass Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        
        temp = self.myPow(x, n/2)
        if n % 2 == 1:
            return temp*temp*x
        elif n % 2 == 0:
            return temp * temp
