Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

那么当遇到不匹配的时候，我们到底是删除左边的字符，还是右边的字符呢，我们的做法是两种情况都要算一遍，只要有一种能返回true，那么结果就返回true。
我们可以写一个子函数来判断字符串中的某一个范围内的子字符串是否为回文串，

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return self.isValid(s, left+1, right) or self.isValid(s, left, right -1)
            else:
                left += 1
                right -= 1
        return True
        
    def isValid(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
