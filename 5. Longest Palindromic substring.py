# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: "cbbd"
# Output: "bb"

解题思路：
字符串中每一个字符都有可能是回文串的中心轴，并且有两种可能 - 以此为轴的回文串是奇数和偶数两种情况。
若回文串字符数是奇数，则从s[i]单个是中心轴，分别从i-1, i+1往左右两边，当两边字符匹配时，移动指针，直到超出边界范围停止或者字符串不匹配停止
若回文串字符数是偶数，那么s[i]与s[i+1]需相等并同时往两边扫，判断条件与奇数相同，L+1 到 R-1是回文左右边界点

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
            
        for i in range(len(s)):
            l = i - 1
            r = i + 1
            while l >=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r-l-1 > len(res):
                res = s[l+1:r]

            l = i
            r = i + 1
            while l >=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r-l-1 > len(res):
                res = s[l+1:r]
        return res
