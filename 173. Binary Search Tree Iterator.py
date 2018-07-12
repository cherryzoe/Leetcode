Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.


Tips:
本题相当于考察了BST的非递归中序遍历
需要maintain一个stack，首先从root开始push入栈直到最左节点
在遍历过程中，如果某个节点存在右儿子，则继续从右儿子开始push入栈直到其最左节点
reference https://www.jianshu.com/p/68e1b84d40e2 

maintain a stack. 
1. push all the left nodes of root into stack ==> smallest node should be on top of the stack
2. pop out from the top node in stack,  read and return the value the node. 
if the node has right child, then treat the node as root and push all the left child into stack 

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.stack else False
        

    def next(self):
        """
        :rtype: int
        """
        current = self.stack.pop()
        res = current.val
        node = current.right
        while node:
            self.stack.append(node)
            node = node.left
        return res

    

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
