# Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example, given a 3-ary tree:


# We should return its level order traversal: 

# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
 

# Note:

# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.
"""

Example for testcase:children is implemented as nested dicitonary
{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},
{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# similar to LC102 bianry tree level order traverse. one more loop to get children from nested structure
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        cur = [root]
        res = []
        while cur:
            nx = []
            res.append([node.val for node in cur])  
            for node in cur:
                if node.children:
                    for child in node.children:
                        nx.append(child)    
            cur = nx
        return res

Clean code: 
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        cur = [root]
        res = []
        while cur: 
            res.append([node.val for node in cur])  
            cur = [child for node in cur for child in node.children if node.children]
        return res
