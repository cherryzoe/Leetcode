class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # 1. There should be no cycle in graph => # edge + 1 == n
        # 2. All nodes in graph should be connected, no node is isolated => travserse and count connected nodes and it should be n 
        
        if len(edges) + 1 != n:
            return False
        if len(edges) < 2:
            return True
          
      # use a dict to save relationships between nodes so that we will get connected nodes from dictionary fast
        mapping = collections.defaultdict()
        for edge in edges:
            mapping[edge[0]] = mapping.get(edge[0], []) + [edge[1]]
            mapping[edge[1]] = mapping.get(edge[1], []) + [edge[0]]

        q = collections.deque([edges[0][0]])
        visited = set([edges[0][0]])
        # travse from a starting node and get all connected node, save all to visited
        # all nodes are connected and be checked and saved in visited, total number should be n
        # if there is no isolated nodes and could not be reached through given node, len(visited) < n
        while q:
            node = q.popleft()
            children = mapping[node]
            for child in children:
                if child not in visited:
                    q.append(child)
                    visited.add(child)
        return len(visited) == n
