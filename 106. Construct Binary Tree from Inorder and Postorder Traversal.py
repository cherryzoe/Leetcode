
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

思路类似于105
后序数组的最后一个元素是根节点。 带入到中序中，以根节点的位置一分为二，左边是左子树，右边是右子树，并且分别得到左右子树的长度。
由于左右子树长度在后序数组中也应与中序中相同，以此为据，后序数组也可以分为左右子树。以此类推递归。
同时根据后序数组与中序数组一起，可以确定树

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if len(postorder) == 0:
            return None
        
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid: -1])

        return root
