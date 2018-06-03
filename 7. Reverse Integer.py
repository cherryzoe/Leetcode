Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Solution1:
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res  = 0
        flag = 1 if x > 0 else -1
        x = abs(x)

        while x:
            digit = x % 10
            res = res * 10 + digit
            x /= 10
        handle overflow issue
        return res*flag if abs(res) < 0x7FFFFFFF else 0
        
  Solution2:
  class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = int(str(x)[::-1]) if x >= 0 else - int(str(-x)[::-1])
        return x if x < 2147483648 and x >= -2147483648 else 0
