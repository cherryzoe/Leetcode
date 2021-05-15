# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 每次返回两个值，节点个数和节点和
class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        self.res =  0.0

        def dfs(root):
            if not root:
                return 0,0

            l_cnt, l_sum = dfs(root.left)
            r_cnt, r_sum = dfs(root.right)

            cur_cnt = 1 + l_cnt + r_cnt
            cur_sum = root.val + l_sum + r_sum 
#           分母加浮点数
            self.res = max(self.res, cur_sum/float(cur_cnt)) 

            return cur_cnt, cur_sum

        dfs(root)
        return self.res
