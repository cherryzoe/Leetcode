In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return -1
        fresh, rotten, cnt = 0, 0, 0
        r,c = len(grid), len(grid[0])
        queue = collections.deque()
        dirs = [(0,1), (-1,0), (0,-1), (1,0)]

       
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    rotten += 1
                    queue.append((i,j, 0))
        
        while queue:
            i,j,cnt = queue.popleft()
            for di, dj in dirs:
                ni,nj = i+di, j+dj
                if not self.isValid(ni, nj, grid):
                    continue
                fresh -= 1
                grid[ni][nj] = 2
                queue.append((ni, nj, cnt+1))
            print cnt, fresh
                
        
        if fresh == 0:
            return cnt
        return -1
    
    def isValid(self, i, j, grid):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1
