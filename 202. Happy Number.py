# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Example: 19 is a happy number

# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

# 解题思路 - 用快慢指针快速判断环
# 分两种情况
# - 一旦到达1往下的值一直保持在1.快慢指针都会停在1
# - 循环一直往复，过程中从未出现结果为1。这种情况下快慢指针会相遇在中间非1的点
# 因此出while的时候就是slow = fast的情况，判断是上面那种即可
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        fast, slow = self.find_square_sum(n), n

        while fast != slow:
            fast = self.find_square_sum(self.find_square_sum(fast))
            slow = self.find_square_sum(slow) 
        return slow == 1

    def find_square_sum(self, n):
        res = 0
        while n:
            digit = n%10
            res += digit * digit
            n /= 10
        return res 

# Idea:
# there are two way to get out of loop:
# 1.  n stays in 1 => happy number
# 2.  n is not 1 but n was occured in loop => create a set to store the history n, once it's show again then it's definitely not happy number
# class Solution(object):
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
