# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true



# 题目大意：
# 给定两个字符串ransomNote和magazine，编写函数判断magazine中的字符是否可以完全包含ransomNote中的字符。

# 注意：可以假设字符串中只包含小写字母。

# 解题思路：
# 利用Python的collections.Counter类统计字符个数，然后做差即可

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        c1 = collections.Counter(ransomNote)
        c2 = collections.Counter(magazine)
        return not c1-c2
