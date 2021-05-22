
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        parent = {} # {child: parent}
        self.target = None
        self.findTargetNode(root, k, parent)

        # start from target, BFS and return first leave node
        # check if left,right and parent is visited and add into q
        # return the first leave node
        q = collections.deque([self.target])
        visited = set()
        visited.add(self.target)
       
        while q:
            cur = q.popleft()
            if not cur.left and not cur.right:
                return cur.val 

            if cur.left and cur.left not in visited:
                visited.add(cur.left)
                q.append(cur.left)

            if cur.right and cur.right not in visited:
                visited.add(cur.right)
                q.append(cur.right)
            
            if parent.get(cur, None) != None and parent[cur] not in visited:
                visited.add(parent[cur])
                q.append(parent[cur])
        
        return 0


    def findTargetNode(self, root, k, parent):
        if not root:
            return

        if root.val == k:
            self.target = root

        if root.left:
            parent[root.left] = root
            self.findTargetNode(root.left, k, parent)

        if root.right:
            parent[root.right] = root
            self.findTargetNode(root.right, k, parent)

