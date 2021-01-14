实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1

解题思路：
滑动窗口

如果加入窗口首字符判断，haystack[i] == needle[0]的时候，如果needle和haystack给定的是空字符，调用needle[0]的时候会报错。因此这种写法需要加特判空字符的情况。

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
   
        len1 = len(haystack)
        len2 = len(needle)
        for i in range(len1-len2+1):
            if haystack[i:i+len2] == needle:
                return i
        return -1
