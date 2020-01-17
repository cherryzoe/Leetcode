Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
          
If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.
https://www.cnblogs.com/grandyang/p/4293853.html

1. Recursion Solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        if root.left:
            self.flatten(root.left)
        if root.right:
            self.flatten(root.right)
            
        temp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = temp
        
