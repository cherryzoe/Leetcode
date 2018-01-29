# Given a binary tree, return the preorder traversal of its nodes' values.

# For example:
# Given binary tree [1,null,2,3],
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].

# Idea:
# 1. If the child node is Null, still push into the stack. While pop out, judege if it's NULL then skip to the next top one on stack.
# 2. root - left(if left has child tree, save left node val into res and push its child node into stack
# 3. left node is on top of right node in stack, so while pop out left is the one prior to right node

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
