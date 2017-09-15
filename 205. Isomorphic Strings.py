# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

# For example,
# Given "egg", "add", return true.

# Given "foo", "bar", return false.

# Given "paper", "title", return true.

# Note:
# You may assume both s and t have the same length.
# 解题思路：
# 1. 建2个字典分别保存s:t 和 t:s的映射关系
# 2. 同时遍历s, t， 并且check是否已存入字典，若字典中没有该字母则存入，若已存在则同时从d1, d2中分别调出t, s 并与t[i], s[i]对比
# 只有当两个都相等时才进入到下一位循环判断，否则返回False结束程序

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = dict(), dict()
        for i in range(len(s)):
#         第一次出错因为没有用get()而是直接用d1[t[i]],这样的话如果调用目标不存在就会报错，而同样情况下get（）则会返回None，不会报错
            source, target = d1.get(t[i]), d2.get(s[i])
            if source is None and target is None:
                d1[t[i]], d2[s[i]] = s[i], t[i]
#                 记住每次比较的对象总是从字典里调出source， target与实际的s[i] t[i]比
            elif source != s[i] or target != t[i]:
                return False
        return True

#     2nd time code also works:
        source, target = dict(), dict()
        for i in range(len(s)):
            if s[i] not in source and t[i] not in target:
                source[s[i]], target[t[i]] = t[i], s[i]
            elif source.get(s[i]) != t[i] or target.get(t[i]) != s[i]:
                return False
        return True
            
