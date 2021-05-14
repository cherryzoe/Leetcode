
# BFS / DFS 的时间复杂度是 O(n^2), n 为城市的数量，需要遍历 n^2 的邻接矩阵

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        # dfs solution:
        # loop through all cites, from 1 - n. 
        # find a city,if it is not visited, -> increase province count and  explore its connected city
        self.n = len(isConnected)
        visited = set()
        cnt = 0
        for i in range(self.n):
            if i not in visited:
                cnt += 1
                self.explore(i, isConnected, visited)
        return cnt 

    def explore(self, i, isConnected, visited):
        visited.add(i)

        for j in range(self.n):
            if isConnected[i][j] == 1 and j not in visited:
                self.explore(j, isConnected, visited)

                # BFS Version                
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        # bfs version
        q = collections.deque()
        n = len(isConnected)
        cnt = 0
        visited = [False for _ in range(n)]

        for i in range(n):
            if visited[i] == False:
                q.append(i)
                visited[i] = True
                cnt += 1

                while q:
                    cur = q.popleft()
                    # visited[cur] = True
                    for j in range(n):
                        nx = isConnected[cur][j]
                        if not visited[j] and nx == 1:
                            q.append(j)
                            visited[j] = True
        return cnt
