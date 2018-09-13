# You are given a binary tree in which each node contains an integer value.

# Find the number of paths that sum to a given value.

# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

# Example:

# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

# Return 3. The paths that sum to 8 are:

# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11

# 双重循环，第一层pathSum遍历每一个节点， 第二层循环sumUp返回某一个节点下子树的可能路径总数

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.sumUp(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def sumUp(self, node, sum):
        res = 0
        if not node:
            return 0
        if node.val == sum:
            res += 1
        if node.left:
            res += self.sumUp(node.left, sum - node.val) 
        if node.right:
            res += self.sumUp(node.right, sum - node.val)
        return res
            
#    一样的代码， 上面的更简洁，下面这种易于理解
class Solution(object):
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        res += self.dfs(root, sum)
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)
        return res
    
    def dfs(self, root, subsum):
        if not root:
            return 0
        cnt = 0
        if subsum == root.val:
            cnt += 1
        cnt += self.dfs(root.left, subsum - root.val)
        cnt += self.dfs(root.right, subsum - root.val)
        return cnt
        
