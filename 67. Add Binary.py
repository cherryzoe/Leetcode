# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".


# 2/20
# Notes:
# 1. initial res as string type so do not need to convert type later. 
#     As string, another benifit is concanate string in sequence from left to right, 
#     so do no need to reverse as list even though we calculate from right to left
# 2. ord() - return unicode int
# 3. str() - int to string
# 4. binary add: n%2 = bit digit n/2 = carrry

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j  = len(a) - 1, len(b) - 1
        s = carry = 0
        res = ''
        while i >= 0 or j >= 0 or carry > 0:
            s = carry
            if i >= 0:
                s += ord(a[i]) - ord('0')
                i -= 1
            if j >= 0:
                s += ord(b[j]) - ord('0')
                j -= 1
            res = str(s%2) + res
            carry = s/2
        return res
    
#1st version: 
# 解题思路：
# 1.注意int与string之间的转换
# 2.binary add的方向是从后往前，所以用string【-1-index】表示
# 3.当所有位运算结束后，carry仍为1时，需要再次往前进一位，增加一个1在最高位的空位
# 4.当前位的结果可以用 a+b%2 得到

class Solution:
# @param a, a string
# @param b, a string
# @return a string
# 75ms
def addBinary(self, a, b):
    result = ''
    index = 0
    
    carry = '0'
    while index < max(len(a), len(b)) or carry == '1':
        num_a = a[-1 - index] if index < len(a) else '0'
        num_b = b[-1 - index] if index < len(b) else '0'
        
        val = self.to_int(num_a) + self.to_int(num_b) + self.to_int(carry)
        result = "%s%s" % (val % 2, result)
        
        carry = '1' if val > 1 else '0'
        index += 1

    return result

def to_int(self, c):
    if c == '1':
        return 1
    elif c == '0':
        return 0
