# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # if not root:
        #     return []
        # res = []
        # q = collections.deque([root])

        # while q:
        #     le = len(q)
        #     for i in range(le):
        #         cur = q.popleft()
        #         if i == le-1:
        #             res.append(cur.val)
        #         if cur.left:
        #             q.append(cur.left)
        #         if cur.right:
        #             q.append(cur.right)
        # return res

        # DFS version - root - right -left

        self.res = []
        self.traverseTree(root, 0)
        return self.res

    def traverseTree(self, root, depth):
        if not root:
            return 
        if len(self.res) <= depth:
            self.res.append(root.val)
            
        self.traverseTree(root.right, depth+1)
        self.traverseTree(root.left, depth+1)
        
