Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


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

    
  
