# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 

# Idea:
# calculate the difference between digit and 'A', chr() function get each digit

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n > 0:
            n -= 1
            res = chr(n%26 + ord('A')) + res
            n = n/26
        return res

