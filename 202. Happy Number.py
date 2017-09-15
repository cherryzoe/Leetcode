Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1


Idea:
there are only two way for each loop:
1.  n stays in 1 => happy number
2.  n is not 1 and in this case n will occured in loop => set a set to store the occured n, once it's show again then it's not happy number
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        st = set()
        while n != 1 and n not in st:
            st.add(n)
            summ = 0
            while n != 0:
                digit = n%10
                summ += digit * digit
                n = n/10
            n = summ
        return n == 1
