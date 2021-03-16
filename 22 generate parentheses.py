# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
思路：
用一个队列来循环，当左括号的个数小于n时，继续加左括号；当右括号的个数小于左括号，加右括号。当左右括号的个数都等于n时，将当前值加入结果。
Iterative solution:
    def generateParenthesis(self, n):
        res = []
        q = collections.deque('(')

        while q:
            cur = q.pop()
            left, right = cur.count('('), cur.count(')')
            if left == n and right == n:
                res.append(cur)
            if left < n:
                q.append(cur + '(')
            if left > right:
                q.append(cur + ')')
        return res 
        
    
Recursive solution:
class Solution(object):        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        s = ''
        if n == 0:
            return 
        self.dfs(res, n, n, s)
        return res 
    
    def dfs(self, res, left, right, s):
        if left > right:
            return
        if left == 0 and right == 0:
            res.append(s)
            return  
        if left > 0:
            self.dfs(res, left-1, right, s + '(')
        if right > 0:
            self.dfs(res, left, right-1, s + ')')

    
  
