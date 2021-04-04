Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.

解题思路：
遍历棋盘，遇到1的情况就从当前grid开始进去做DFS，探索4个方向，获取当前岛屿的面积，同时维护和更新最大岛屿变量
DFS里面，首先是终止条件-约界情况 + 非岛屿情况 -》返回0
然后就是处理当前是‘1’的情况 -》 把1设为0，表示已经被访问过了，避免重复访问。当前的面积是1，向四个方向分别探索，如果存在，则向上返回1，否则返回0

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j)
                    max_area = max(max_area, area)
        return max_area 

    def dfs(self, grid, row, col):
        # out of range 
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 0
        # visted or not island 
        if grid[row][col] != 1:
            return 0
        # current grid is 1, we set it to 2 as visited and explore its 4 directions
        grid[row][col] = 2
        d1 = self.dfs(grid, row + 1, col)
        d2 = self.dfs(grid, row-1, col) 
        d3 = self.dfs(grid, row, col+1) 
        d4 = self.dfs(grid, row, col -1)
        return 1 + d1 + d2 + d3 + d4 
          
        
