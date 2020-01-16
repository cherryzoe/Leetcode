# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

# Note:

# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.
# Example:

# Input: root = [4,2,5,1,3], target = 3.714286

#     4
#    / \
#   2   5
#  / \
# 1   3

# Output: 4

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# solution 1: with extra space
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return 
        path = []
        while root:
            path.append(root.val) 
#           先存当前节点的值的时候必须保证当前节点不是None否则 None.val会报错，因此在while check过了进入循环后，进行移动操作前，第一时间存
            root = root.left if root.val > target else root.right
        
        return min(path, key = lambda x: abs(target - x))

# solution 2: 推荐 O(1) space
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        res = root.val
        while root:
            if abs(root.val - target) < abs(res - target):
                res = root.val
            root = root.left if target < root.val else root.right
        return res

    # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return None
        
        min_diff = sys.maxint
        close_val = root.val
        
        while root:
            diff = root.val - target
            if abs(diff) < min_diff:
                close_val = root.val
                min_diff = abs(diff)
                
            if diff == 0:
                return root.val
            if diff > 0:
                root = root.left
            else:
                root = root.right
                
        return close_val
