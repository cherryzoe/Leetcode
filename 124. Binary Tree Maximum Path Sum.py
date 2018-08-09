# Given a binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some 
# starting node to any node in the tree along the parent-child connections. 
# The path must contain at least one node and does not need to go through the root.

# For example:
# Given the below binary tree,

#        1
#       / \
#      2   3
# Return 6.

reference: http://bangbingsyb.blogspot.com/2014/11/leetcode-binary-tree-maximum-path-sum.html 

 解题思路：
递归搜索每颗子树，对于当前节点node，可以看做是每条路径的必经点，也是每颗子树的根。 
node有两种选择：
1. 到node为止，不继续往下走， 那么可增加值为0
2. 往下走， 可增加值 = 左子树 + 右子树(分别递归其子树得到最大值）+本身的值 

- 当前路径是node.left => node = >node.right（方向可逆）, 但一定只能是单条路径过来，即每个子节点只能连接一个其下面的子节点。 
  因此增量是 node.left.value + node.right.value + node.value
  
- 如果递归下去，对于root.left下面也只能是单一无分叉路径，因此只能从root.left.left和root.left.right中选取其一较大值： max(left,right) + self

这道求二叉树的最大路径和是一道蛮有难度的题，难就难在起始位置和结束位置可以为任意位置，我当然是又不会了，于是上网看看大神们的解法，像这种类似数的遍历的题，一般来说都需要用DFS来求解，我们先来看一个简单的例子：

    4
   / \
  11 13
 / \
7   2
由于这是一个很简单的例子，我们很容易就能找到最长路径为7-11-4-13，那么怎么用递归来找出正确的路径和呢？根据以往的经验，树的递归解法一般都是递归到叶节点，然后开始边处理边回溯到根节点。那么我们就假设此时已经递归到结点7了，那么其没有左右子节点，所以如果以结点7为根结点的子树最大路径和就是7。然后回溯到结点11，如果以结点11为根结点的子树，我们知道最大路径和为7+11+2=20。但是当回溯到结点4的时候，对于结点11来说，就不能同时取两条路径了，只能取左路径，或者是右路径，所以当根结点是4的时候，那么结点11只能取其左子结点7，因为7大于2。所以，对于每个结点来说，我们要知道经过其左子结点的path之和大还是经过右子节点的path之和大。那么我们的递归函数返回值就可以定义为以当前结点为根结点，到叶节点的最大路径之和，然后全局路径最大值放在参数中，用结果res来表示。

在递归函数中，如果当前结点不存在，那么直接返回0。否则就分别对其左右子节点调用递归函数，由于路径和有可能为负数，而我们当然不希望加上负的路径和，所以我们和0相比，取较大的那个，就是要么不加，加就要加正数。然后我们来更新全局最大值结果res，就是以左子结点为终点的最大path之和加上以右子结点为终点的最大path之和，还要加上当前结点值，这样就组成了一个条完整的路径。而我们返回值是取left和right中的较大值加上当前结点值，因为我们返回值的定义是以当前结点为终点的path之和，所以只能取left和right中较大的那个值，而不是两个都要，参见代码如下
                         
                         
                         
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
