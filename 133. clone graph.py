
visted - 字典，记录老节点和新节点的映射关系 visted = { Node(node.val, node.neighbers) : newNode(newNode.val, newNeighbers 初始为[])}注意存的是Node这个结构而不是一个值而已
顺藤摸瓜，通过给定的输入节点，利用一个queue，遍历到节点的邻居，把邻居一一摸索清楚之后，邻居的邻居，这样整个图是联通的，可以搜遍所有节点，像linkedlist一样。

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        visited = {}

        def bfs(node):
            if not node:
                return

            queue = collections.deque()
            
            newNode = Node(node.val, [])
            visited[node] = newNode
            queue.appendleft(node)

            while queue:
                temp = queue.pop()
                for n in temp.neighbors:
                    if n not in visited:
                        visited[n] = Node(n.val, [])
                        queue.appendleft(n)
                    newNeighbor = visited[temp].neighbors
                    newNeighbor.append(visited[n])

            return newNode
        
        return bfs(node)
