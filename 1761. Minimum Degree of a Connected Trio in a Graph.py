class Solution(object):
    def minTrioDegree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # brute force solution:
        # edge is 2 dimenssion array to save the edge between 2 nodes,
        # edge[x][y] = 1 means there is edge connection between X and Y
        # other words, if there is edge between X and Y, both edge[x][y] and edge[y][x] should be set as 1 
        
        # degree is 1 dimenssion array to save degree of each node
        
        # iterate through edge matrix with 3 variable i, j [i+1:], k [j+1:] - once find connected trio, 
        # in other word is edge[i][j] = 1 and edge[j][k] = 1 and edge[i][k] = 1
        # get its out degree = sum of 3 nodes' degree - 6(internal degree) update result when needed
        edge = [[0 for i in range(n+1)] for j in range(n+1)]
        degree = [0 for i in range(n+1)]
        res = float('inf')

        for x,y in edges:
            edge[x][y] = 1
            edge[y][x] = 1
            degree[x] += 1
            degree[y] += 1
        
        for i in range(1, n+1):
            if res == 0:
                break
            for j in range(i+1, n+1):
                for k in range(j+1, n+1):
                    if edge[i][j] and edge[j][k] and edge[i][k]:
                        res = min(res, degree[i] + degree[j] + degree[k] - 6)
        return -1 if res == float('inf') else res 

