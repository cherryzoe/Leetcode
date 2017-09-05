# Write a function to find the longest common prefix string amongst an array of strings.

# 解题思路：
# 1. 找出最短的字符串，作为标准去跟其他的字符串比较。 
# 2. 如果最短字符串长度为0，则结果为空。
# 3. 与list中其他字符串比较前，要判断是否为本身的情况，需要直接跳掉下一个循环
# 4. 使用slice之前一定要保证index不会out of range

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
#         找出最短的字符串，作为标准去跟其他的字符串比较
        minstr = strs[0]
        minlen = len(strs[0])
        for s in strs:
            if len(s) < minlen:
                minstr = s
                minlen = len(s)
#         若最短字符串是一个空字符串，则结果为空字符串，因为不可能有其他非空字符串跟他有公共字符
        if minlen == 0:
            return ''
        for s in strs:
#         判断是否为本身的情况，需要直接跳掉下一个循环
            if s == minstr: continue
#             判断最小是否是另一个字符串的子集，若是则直接返回最小即可。
            if s[:len(minstr)] != minstr:
                for i in range(len(minstr)):
                    if s[i] != minstr[i]:
                        break
                minstr = s[:i]
        return minstr
