Invert a binary tree.
     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1


解题思路：
BFS - 用stack来实现所有节点的遍历。 
1. 将节点放入栈后，读取最后一个值，
2. 将其左右节点互换位置后，再将左右节点依次放入栈
3. 重复以上循环直至栈为空， 所有节点都遍历过
通常情况下，当二叉树用栈解决时，步骤是 
将第一个节点（root）放入栈，然后弹出，对其左右节点进行操作，再将左右节点存入栈，重复上一个循环

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            left = node.left
            node.left = node.right
            node.right = left
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root


