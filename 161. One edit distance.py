给定两个字符串 s 和 t，判断他们的编辑距离是否为 1。

注意：

满足编辑距离等于 1 有三种可能的情形：

往 s 中插入一个字符得到 t
从 s 中删除一个字符得到 t
在 s 中替换一个字符得到 t
示例 1：

输入: s = "ab", t = "acb"
输出: true
解释: 可以将 'c' 插入字符串 s 来得到 t。
示例 2:

输入: s = "cab", t = "ad"
输出: false
解释: 无法通过 1 步操作使 s 变为 t。
示例 3:

输入: s = "1203", t = "1213"
输出: true
解释: 可以将字符串 s 中的 '0' 替换为 '1' 来得到 t。

解题思路：
s 加一和减一得到t 可以通过兑换s,t的对应关系来用同一种方法验证
遍历短的数组s,遇到不一样的时候，跳过，比较后面的是否相同

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls = len(s)
        lt = len(t)

        if ls > lt:
            return self.isOneEditDistance(t, s)
        
        if lt - ls > 1:
            return False 

        for i in range(len(s)):
            if s[i] != t[i]:
                if lt == ls:
                    return s[i+1:] == t[i+1:]
                else:
                    return s[i:] == t[i+1:]
        # 遍历完所有s中的字符串后，并且一一跟t中对应位置元素相等，此时如果t中还存在未被遍历到的元素，那么只有当t中还剩最后一个元素（无论该元素是什么值）才符合条件。
        return ls + 1 == lt
         
