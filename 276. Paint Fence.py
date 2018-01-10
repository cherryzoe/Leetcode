There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        if n == 0:
            return 0
        if n == 1:
            return k
        
        same = k
        diff = k * (k-1)
        
        for i in range(3, n+1):
            prevDiff = diff
            diff = (same + diff) * (k-1)
            same = prevDiff 
        return same + diff
        
Solution 2: O(n) space
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        dp = [0] * n
        dp[0] = k
        dp[1] = k*k
        for i in range(2, n):
            dp[i] = (k-1) * (dp[i -1] + dp[i -2])
        return dp[n-1]
