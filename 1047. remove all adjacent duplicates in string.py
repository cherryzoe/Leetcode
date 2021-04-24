
# 题目限定了重复的长度为2，所以可以用栈来保存元素，
# 每次遇到一个新元素，跟栈顶元素吧比较，相同则pop()出栈顶元素，两者抵消。不同则入栈
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for s in S:
            if stack and stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
        return ''.join(stack)
