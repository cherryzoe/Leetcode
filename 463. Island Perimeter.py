# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

# Example:

# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Answer: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below:

# Tips:

#   每次查看右边和下面一个也对，矩阵问题要注意边界条件
    class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        cnt, repeat = 0,0
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    cnt += 1
                    if i+1 < row and grid[i+1][j]:
                        repeat +=1
                    if j+1 < col and grid[i][j+1]:
                        repeat += 1
        return cnt*4 - repeat*2

 # 只需要计算为1的方格数量和重复的边数即可. 为防止重复计算重合边, 每次只往回查看, 也就是如果一个方格为1, 只查看左边和上边的方格是否为1.
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        repeat = 0
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    cnt += 1
                    if i != 0 and grid[i-1][j] == 1:
                        repeat += 1
                    if j != 0 and grid[i][j-1] == 1:
                        repeat += 1
        return cnt * 4 - repeat * 2
# DFS solution
# 岛屿的周长就是岛屿方格和非岛屿方格相邻的边的数量。注意，这里的非岛屿方格，既包括水域方格，也包括网格的边界
    class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    return self.explore(i, j, grid)
        return 0 

    def explore(self, r, c, grid):
#       网格边界，返回，并且+1
        if r <0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return 1
#       水域，返回，并且+1
        if grid[r][c] == 0:
            return 1
#       岛屿，且已经被访问过，直接返回
        if grid[r][c] == 2:
            return 0
        # 排除选项后剩下grid == 1的情况，当前是岛屿，进行四方向探索
        # 先将当前岛屿设置成2，避免重复访问
        grid[r][c] = 2
        d1 = self.explore(r+1,c,grid)
        d2 = self.explore(r-1,c,grid)
        d3 = self.explore(r, c-1,grid)
        d4 = self.explore(r,c+1,grid)
        return d1 + d2 + d3 + d4
