

recursion:

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        if num < 10:
            return num
        digits = 0
        while num:
            digits += num % 10
            num /= 10
        return self.addDigits(digits)
        
Non-Recursion:
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        while num >= 10:
            temp = 0
            while num:
                temp += num % 10
                num /= 10
            num = temp
        return num
