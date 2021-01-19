一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

解题思路：
障碍物的地方应该是0，表示无法到达。其余的初始化边界行列为1.
遍历表格的时候，外层大循环是行，内层小循环是列。不能搞反了。

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]

        for i in range(col):
            if obstacleGrid[0][i]:
                break
            dp[0][i] = 1
        for j in range(row):
            if obstacleGrid[j][0]:
                break
            dp[j][0] = 1
        
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:    
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
