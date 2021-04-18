"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):


    def treeToDoublyList(self, root):
        """
from types import prepare_class
from types import prepare_class
        :type root: Node
        :rtype: Node
        """
        if not root:
            return 
        dummy = Node(-1,None,None)
        self.pre = dummy 

        def inOrder(root):
            if not root:
                return 
            inOrder(root.left)

            self.pre.right = root
            root.left = self.pre
            # pre = root
            self.pre = self.pre.right 

            inOrder(root.right)

        inOrder(root)
        dummy.right.left = self.pre
        self.pre.right = dummy.right 
        return dummy.right
        
    
   
