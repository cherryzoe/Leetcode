# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        if not root:
            return []
        self.newRoot = None
        self.res = []
        self.findTarget(root, target, None)
        self.dfs(target, k)
        self.dfs(self.newRoot, k-1)
        return self.res

    # find target node, split the tree between target node and it's parent node
    # original link between parent & target node will be disconnected, new link set up between parent & parent's parent 
    def findTarget(self, root, target, parent):
        if not root:
            return 0
        if root == target:
            self.newRoot = parent 
            return 1
    # 判断target是在左子树还是右子树，如果是左子树，那么把指向左子树的链接重新指向父节点。若target存在于右子树，则把指向右子树的链接重新指向父节点
        if self.findTarget(root.left, target, root):
            root.left = parent
            return 1
        if self.findTarget(root.right, target, root):
            root.right = parent        
            return 1
        return 0

    # find nodes to root's distance = k
    def dfs(self, root, k):
        if not root:
            return 
        if k == 0:
            self.res.append(root.val)

        l = self.dfs(root.left, k-1)
        r = self.dfs(root.right, k-1)
