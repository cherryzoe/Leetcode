# 解题思路：遍历数组，遇到数字存入栈，遇到运算符，从栈中取出2元素，算出结果，再压入栈中
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t[-1].isdigit():
                stack.append(int(t))
            else:
                if stack: x = stack.pop()
                if stack: y = stack.pop()
                if t == '+':
                    stack.append(x+y)
                elif t == '*':
                    stack.append(x*y)
                elif t == '-':
                    stack.append(y-x)
                elif t == '/':
                    stack.append(int(y/float(x)))
        return stack[-1]
