# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3
# 思路
# 我们遍历矩阵的每一个点，对每个点都尝试进行一次深度优先搜索，如果搜索到1，就继续向它的四周搜索。
# 同时我们每找到一个1，就将其标为0，这样就能把整个岛屿变成0。我们只要记录对矩阵遍历时能进入多少次搜索，就代表有多少个岛屿。
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.exploreIsland(grid, row, col)
                    cnt += 1
        return cnt
    
    def exploreIsland(self, grid, row, col):
        grid[row][col] = '0'
        if row > 0 and grid[row-1][col] == '1':
            self.exploreIsland(grid, row-1, col)
        if col > 0 and grid[row][col - 1] == '1':
            self.exploreIsland(grid, row, col -1)
        if row < len(grid)-1 and grid[row+1][col] == '1':
            self.exploreIsland(grid, row+1, col)
        if col < len(grid[0])-1 and grid[row][col+1] == '1':
            self.exploreIsland(grid, row, col+1)
            
     #BFS version
    class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        cnt = 0
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    cnt += 1
        return cnt
    
    
    def bfs(self, grid, x, y):
        grid[x][y] = '0'
        q = collections.deque([(x, y)])
        while q:
            x,y = q.popleft()
            for delta_x, delta_y in [(0,1), (0,-1), (1,0), (-1,0)]:
                x_next = delta_x + x
                y_next = delta_y + y
                if not self.isValid(grid, x_next, y_next):
                    continue
                q.append((x_next, y_next))
                grid[x_next][y_next] = '0'
                    
        
    def isValid(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        return 0 <= x < n and 0 <= y < m and grid[x][y] == '1'
    
#  后续 Follow Up
# Q:如何找湖的数量呢？湖的定义是某个0，其上下左右都是同一个岛屿的陆地。
# A:我们可以先用Number of island的方法，把每个岛标记成不同的ID，然后过一遍整个地图的每个点，
# 如果是0的话，就DFS看这块连通水域是否被同一块岛屿包围，如果出现了不同数字的陆地，则不是湖。
# https://segmentfault.com/a/1190000003753307
public class NumberOfLakes {
    
    public static void main(String[] args){
        NumberOfLakes nof = new NumberOfLakes();
        int[][] world = {{1,1,1,0,1},{1,0,0,1,0},{1,1,1,1,1,},{0,1,1,0,1},{0,1,1,1,1}};
        System.out.println(nof.numberOfLakes(world));
    }
    
    public int numberOfLakes(int[][] world){
        int islandId = 2;
        for(int i = 0; i < world.length; i++){
            for(int j = 0; j < world[0].length; j++){
                if(world[i][j] == 1){
                    findIsland(world, i, j, islandId);
                    islandId++;
                }
            }
        }
        int lake = 0;
        for(int i = 0; i < world.length; i++){
            for(int j = 0; j < world[0].length; j++){
                if(world[i][j] == 0){
                    // 找到当前水域的邻接陆地编号
                    int currId = 0;
                    if(i > 0) currId = (world[i - 1][j] != 0 ? world[i - 1][j] : currId);
                    if(j > 0) currId = (world[i][j - 1] != 0 ? world[i][j - 1] : currId);
                    if(i < world.length - 1) currId = (world[i + 1][j] != 0 ? world[i + 1][j] : currId);
                    if(j < world[0].length - 1) currId = (world[i][j + 1] != 0 ? world[i][j + 1] : currId);
                    // 如果该点是湖，加1
                    if(findLake(world, i, j, currId)){
                        lake++;
                    }
                }
            }
        }
        return lake;
    }
    
    private boolean findLake(int[][] world, int i, int j, int id){
        // 将当前水域标记成周边岛屿的数字
        world[i][j] = id;
        // 找上下左右是否是同一块岛屿的陆地，如果是水域则继续DFS，如果当前水域是边界也说明不是湖
        boolean up = i != 0 
                && (world[i - 1][j] == id 
                || (world[i - 1][j] == 0 && findLake(world, i - 1, j, id)));
        boolean down = i != world.length - 1 
                && (world[i + 1][j] == id 
                || (world[i + 1][j] == 0 && findLake(world, i + 1, j, id)));
        boolean left = j != 0 
                && (world[i][j - 1] == id 
                || (world[i][j - 1] == 0 && findLake(world, i, j - 1, id)));
        boolean right = j != world[0].length - 1 
                && (world[i][j + 1] == id 
                || (world[i][j + 1] == 0 && findLake(world, i, j + 1, id)));
        return up && down && right && left;
    }
    
    private void findIsland(int[][] world, int i, int j, int id){
        world[i][j] = id;
        if(i > 0 && world[i - 1][j] == 1) findIsland(world, i - 1, j, id);
        if(j > 0 && world[i][j - 1] == 1) findIsland(world, i, j - 1, id);
        if(i < world.length - 1 && world[i + 1][j] == 1) findIsland(world, i + 1, j, id);
        if(j < world[0].length - 1 && world[i][j + 1] == 1) findIsland(world, i, j + 1, id);
    }
}
