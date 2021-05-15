# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# 这道求二叉树的最小共同父节点的题是之前那道 Lowest Common Ancestor of a Binary Search Tree 的 Follow Up。跟之前那题不同的地方是，
# 这道题是普通是二叉树，不是二叉搜索树，所以就不能利用其特有的性质，我们只能在二叉树中来搜索p和q，然后从路径中找到最后一个相同的节点即为父节点，可以用递归来实现，
# 在递归函数中，首先看当前结点是否为空，若为空则直接返回空，若为p或q中的任意一个，也直接返回当前结点。否则的话就对其左右子结点分别调用递归函数，
# 由于这道题限制了p和q一定都在二叉树中存在，那么如果当前结点不等于p或q，p和q要么分别位于左右子树中，要么同时位于左子树，或者同时位于右子树，那么我们分别来讨论：

# - 若p和q分别位于左右子树中，那么对左右子结点调用递归函数，会分别返回p和q结点的位置，而当前结点正好就是p和q的最小共同父结点，直接返回当前结点即可，这就是题目中的例子1的情况。

# - 若p和q同时位于左子树，这里有两种情况，一种情况是 left 会返回p和q中较高的那个位置，而 right 会返回空，所以最终返回非空的 left 即可，这就是题目中的例子2的情况。还有一种情况是会返回p和q的最小父结点，就是说当前结点的左子树中的某个结点才是p和q的最小父结点，会被返回。

# - 若p和q同时位于右子树，同样这里有两种情况，一种情况是 right 会返回p和q中较高的那个位置，而 left 会返回空，所以最终返回非空的 right 即可，还有一种情况是会返回p和q的最小父结点，就是说当前结点的右子树中的某个结点才是p和q的最小父结点，会被返回

# 终止条件：
# 当越过叶节点，则直接返回 nullnull ；
# 当 rootroot 等于 p, qp,q ，则直接返回 rootroot ；

# 递推工作：
# 开启递归左子节点，返回值记为 leftleft ；
# 开启递归右子节点，返回值记为 rightright ；

# 返回值： 根据 leftleft 和 rightright ，可展开为四种情况；
# 当 leftleft 和 rightright 同时为空 ：说明 rootroot 的左 / 右子树中都不包含 p,qp,q ，返回 nullnull ；
# 当 leftleft 和 rightright 同时不为空 ：说明 p, qp,q 分列在 rootroot 的 异侧 （分别在 左 / 右子树），因此 rootroot 为最近公共祖先，返回 rootroot ；
# 当 leftleft 为空 ，rightright 不为空 ：p,qp,q 都不在 rootroot 的左子树中，直接返回 rightright 。具体可分为两种情况：
# p,qp,q 其中一个在 rootroot 的 右子树 中，此时 rightright 指向 pp（假设为 pp ）；
# p,qp,q 两节点都在 rootroot 的 右子树 中，此时的 rightright 指向 最近公共祖先节点 ；
# 当 leftleft 不为空 ， rightright 为空 ：与情况 3. 同理；

'''
 
Traverse through the tree
once matched the node.val == p/q.val, return the node
For each node in the tree, check return vlaue from both left and right

e.g. example 1
for node 3, 
its left tree return 5 as node p=5 exists in left Tree
its right tree return 1 as node q=1 exists in right tree
when left and right both return valid node => 3 is the LCA of p and q

e.g. example 2
when p and q exist in same subtree, and p is root of the tree => p is LCA of p and q
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None 
        
        if root == p or root == q:
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        # if l == None: left subtree has no p or q
        # if r == None: right subtree has no p or q

        # p and q exist seperatly in left and right subtree => current node is the LCA of p and q
        if l and r:
            return root 
        
        # only l returns value => p and q both in left, LCA must be in left, return left
        if l: 
            return l 
        # only r returns value => p and q both in right, LCA must be in right, return right
        if r:
            return r 

         
'''
升级版
------
如果题目中p,q有可能不在数中，用以下代码
this code applies to situation when p and q are not in the tree
when we say p exist in the tree, we check and return True 
if p in left subtree
or p in right subtree
or p is the root node

assume at node X, and its left and right both return true for the first time(travserse buttom up)
X is the lowest common ancester 
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.res = None 
        # a/b - boolean value represent if p/q exist in the subtree or not 
        a, b = self.checkExist(root, p, q)
        if a and b:#when both p and q exist in the tree, return LCA. otherwise return None
            return self.res
        return None
        
    def checkExist(self, root, p, q):
        if not root:
            return False, False
        
        a_l, b_l = self.checkExist(root.left, p, q)
        a_r, b_r = self.checkExist(root.right, p, q)
        # check if a/b exist in the subtree(of which root is root.left), if yes, return true

        # check a subtree with root as its root, if exists in its left tree or right tree or is the root node
        a = a_l or a_r or root == p
        b = b_l or b_r or root == q

        # when both a and b return True for the first time, when res has not been set yet, root is our reult
        if a and b and self.res == None:
            self.res = root
        # return boolean(if a exist in the tree, if b exists in the tree)
        return a, b       
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        # 对于例子2中p=5,q=4的情况，当左边遍历到5的时候，就会返回值5，不会继续往下走到4，因为这种情况下，4位于5下面，5就是（4，5）的最小公共祖先
        if root.val == q.val or root.val == p.val:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # 如果左右子树中存在p或者q,那么就会有返回值，若不存在，返回None。根据此性质可判断，当左右子树都有值时，当前root是LCA    
        if left and right:
            return root
        return left or right
