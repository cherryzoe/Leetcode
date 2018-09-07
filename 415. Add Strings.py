Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ''
        i,j, carry = len(num1)-1, len(num2)-1, 0
        
        while i >= 0 or j >= 0 or carry ==1:
            n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            n2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            digit = (n1 + n2 + carry) % 10
            carry = (n1 + n2 + carry) / 10    # 先算digit 后算carry， 因为carry的值会在此轮改变，而digit用到的carry必须是上一轮的        
            res = str(digit) + res
            i -= 1
            j -= 1
        return res
        
