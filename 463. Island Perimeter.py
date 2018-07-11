# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

# Example:

# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Answer: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below:

# Tips:
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
