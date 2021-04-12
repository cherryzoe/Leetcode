Given a node in a binary search tree, return the in-order successor of that node in the BST. If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than node.val.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
 

Example 1:


Input: tree = [2,1,3], node = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both the node and the return value is of Node type.

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # 情况1：有右孩子
        # 直接返回右子树的最min值
        # 情况2：没右孩子
        # 找第一个比node.val值大的parent节点

        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        else:
            val = node.val
            while node.parent:
                node = node.parent
                if node.val > val:
                    return node
        
