class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        res = 0
        mapping = collections.defaultdict()
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            mapping[n1] = mapping.get(n1, []) + [n2]
            mapping[n2] = mapping.get(n2, []) + [n1]

        q = collections.deque()
        visited = set()
        for i in range(n):
            if i not in visited:
                q.append(i)
                visited.add(i)
                res += 1

                while q:
                    cur = q.popleft()
                    neighbors = mapping.get(cur, [])
                    for nei in neighbors:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
        return res

