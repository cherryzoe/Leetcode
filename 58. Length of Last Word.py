# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# For example, 
# Given s = "Hello World",
# return 5.

# 解题思路：
# 1. 用split（）而不是split（‘ ‘），因为前者将多个连续空格视为一个，两种得出的结果不同
# 2. return的时候先考虑是0的情况，否则可能报错
# 3. 当不能肯定字符串是否为空的时候，不能用slice调用 word[-1]， 别问我怎么知道的 

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = s.split()
        return 0 if len(word) == 0 else len(word[-1])
