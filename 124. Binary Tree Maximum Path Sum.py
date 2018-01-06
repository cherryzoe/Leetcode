Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some 
starting node to any node in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.

解题思路：
递归搜索每颗子树，对于当前节点node，可以看做是每条路径的必经点，也是每颗子树的根。 
node有两种选择：
1. 到node为止，不继续往下走， 那么可增加值为0
2. 往下走， 可增加值 = 左子树 + 右子树(分别递归其子树得到最大值）+本身的值 

- 当前路径是node.left => node = >node.right（方向可逆, 只能是单条无枝杈路径过来。 
  因此增量是 node.left.value + node.right.value + node.value
  
- 如果递归下去，对于root.left下面也只能是单一无枝杈路径，因此只能从root.left.left和root.left.right中选取其一较大值： max(left,right) + self

lass Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """      
        Solution.maxValue = None
        self.maxPathDown(root)
        return Solution.maxValue
    
    def maxPathDown(self, node):
        if not node:
            return 0
        
        left = max( 0, self.maxPathDown(node.left))
        right = max( 0, self.maxPathDown(node.right))
        Solution.maxValue = max(Solution.maxValue, left + right + node.val)
        return max(left, right) + node.val
