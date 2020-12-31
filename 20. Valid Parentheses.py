# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


# 解题思路：
# 1. 输入分三种情况： 
#   - 左括号： 放入stack中
#   - 右括号： 从stack中pop出最上面的值，并且比较是否是一对。 注意在pop之前需要判断此时stack是否为空，若空则也说明数量不对称
#   - 其他符号： 直接返false
#  2. 用dictionary构造数据结构，存放左右括号，并且用value 与 keys 进行索引和关联 
 
# 最后的判断条件是stack里面的元素全部配对成功，也就是stack为空
 class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = {'(':')', '[':']', '{':'}'}
        stack = []

        for i in range(len(s)):
            if s[i] in left:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                le = stack.pop()
                if left[le] != s[i]:
                    return False
        return not stack 
 
 
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = { ')':'(', ']':'[', '}':'{' }
        stack = []
        for i in s:
            if i in match.values():
                stack.append(i)
            elif i in match.keys():
                if len(stack) == 0 or match[i] != stack.pop():
                    return False
            else:
                return False
        return len(stack) == 0
       
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in s:
            if i in dic:
                stack.append(i)
            else:
                if not stack or dic[stack.pop()] != i:
                    return False
        return not stack
