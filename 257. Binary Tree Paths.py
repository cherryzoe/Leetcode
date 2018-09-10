Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

solution 1: DFS
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if root:
            self.helper(root, '', res)
        return res
    
    def helper(self, root, path, res):
        if not root.left and not root.right:
            res.append(path + str(root.val))
        if root.left:
            self.helper(root.left, path + str(root.val) + '->', res)
        if root.right:
            self.helper(root.right, path + str(root.val) + '->', res)
            
            
