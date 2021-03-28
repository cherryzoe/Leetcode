Given a string s, return true if a permutation of the string could form a palindrome.

Example 1:

Input: s = "code"
Output: false

解题思路： 统计每个字符出现的次数，最多只能有一个字符出现奇数次

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cnt = 0
        counts = collections.Counter(s)
  
        for c in counts:
            if counts[c] % 2 != 0:
                cnt += 1
                if cnt > 1:
                    return False
        return True
