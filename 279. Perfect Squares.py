# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# Example 1:

# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

# Solution1 Numberic Theory
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n%4 == 0:
            n /= 4
        if n%8 == 7:
            return 4
        a的范围必须是[0，sqrt(n)]，注意右边界必须取到，否则 n=2时会直接跳过for循环返回3
        for a in range(0, int(math.sqrt(n))+1):
            b = int(math.sqrt(n - a*a))
            if b * b + a *a == n:
                return 1 if not b or not a else 2 
        return 3 

# Solution2 DP:
# python is overtime for this solution
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        dp = [n] * (n+1)
        for i in range(int(n**0.5)+1):
            dp[i*i] = 1
                  
        for i in range(1, n+1):
            for j in range(1, int((n-i)**0.5)+1):
                dp[i + j*j] = min(dp[i] +1, dp[i+j*j])
                print dp
        return dp[-1]
