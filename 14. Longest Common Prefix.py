# Write a function to find the longest common prefix string amongst an array of strings.

update on 4/24/2021
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 取第一个字符串作为基准，跟其他的一一比较
        res = strs[0]
        for i in range(1, len(strs)):
            l1 = len(res)
            l2 = len(strs[i])
            j = 0
            # 循环体内符合条件，不断增加
            while j < min(l1, l2) and res[j] == strs[i][j]:
                j += 1
            # 出循环体，更新并判断 - 越界或者不等
            res = res[:j]
            if not res:
                return ''
        return res


# 解题思路：
# 1. 找出最短的字符串，作为标准去跟其他的字符串比较。 
# 2. 如果最短字符串长度为0，则结果为空。
# 3. 与list中其他字符串比较前，要判断是否为本身的情况，需要直接跳掉下一个循环
# 4. 使用slice之前一定要保证index不会out of range

Update on 12/10/2017
solution 2:
 def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        
        n = zip(*strs) #Unzip the strings in the list into tuples of characters
        for i,v in enumerate(n):
            if len(set(v)) > 1:
                return strs[0][:i]
            else:
                 return min(strs)
           


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
# 找出最短的字符串，作为标准去跟其他的字符串比较
# 调用 strs[0]的时候要考虑0是否在范围内，index out of range的情况，即当输入是空集合【 】。 这种情况跟【“”】空字符串不同，区别在于长度。
        minstr = strs[0]
        minlen = len(strs[0])
        for s in strs:
            if len(s) < minlen:
                minstr = s
                minlen = len(s)
                
#若最短字符串是一个空字符串，则结果为空字符串，因为不可能有其他非空字符串跟他有公共字符
        if minlen == 0:
            return ''
        for s in strs:
            
# 判断是否为本身的情况，需要直接跳掉下一个循环
            if s == minstr: continue
        
# 判断最小是否是另一个字符串的子集，若是则直接返回最小即可。
            if s[:len(minstr)] != minstr:
                for i in range(len(minstr)):
                    if s[i] != minstr[i]:
                        break
                minstr = s[:i]
        return minstr
