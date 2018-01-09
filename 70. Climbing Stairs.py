You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output:  2
Explanation:  There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output:  3
Explanation:  There are three ways to climb to the top.

1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Idea:
Basicly it's Fabonacci array. The final step is just two option: 1 step or 2 step. Those two option are totally isolated with each other. 
If we take one, it will not affect the other one. so we can say the final result is the sum of those two options.
tranfer formula: f(n) = f(n-1) + f(n-2)
initial state: f(1) = 1   f(2) = 2(two options to reach step 2: 1+1 or 2)

O(n) space
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        dp = [0 for i in range(n+1)]
        
        dp[1], dp[2] = 1, 2 
        # Be careful when we assian value for dp[2], we need to look back to the array initializtion. 
        # Only when n>1 and dp has dp[2]. if n == 1 and dp only has dp[0] and dp[1]. everything out of range will be error.
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

Linear space
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n ==1:
            return 1
        if n == 2:
            return 2
        a,b = 1,2
        for i in range(3,n+1):
            c = a + b
            a = b
            b = c
        return c
