# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example 1:
# [[1,3,1],
#  [1,5,1],
#  [4,2,1]]
# Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        
#         初始化矩阵一定是先初始化一个长度为col的数组，再将此数组重复row次
        dp = [[0 for i in range(col)] for j in range(row)]
    
#         一定要考虑初始值，特别是这里的初始值不是0
        dp[0][0] = grid[0][0]
    
        for i in range(1, row):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, col):
            dp[0][j] = dp[0][j-1] + grid[0][j]
             
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
#                 到 grid[i][j]的累积路径和有两种选择： 从【i-1][j]过来，或是从[i][j-1]过来。选二者较小者 + 本身节点的值
        return dp[-1][-1]
