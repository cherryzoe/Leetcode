Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:


解题思路：
BST的中序输出一定是单调递增的数组
题目给定的输入是一个单调递增的数组，去中点为根节点，以此分割数组左半边是左子树，右半边为右子树
继续递归左右两边，分别取各自中点继续递归子树，
递归终止条件：直到空集或者左右边界交叉，说明所有子集都已经被递归到了，返回None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return []
        return self.helper(0, len(nums)-1, nums)

    def helper(self, left, right, nums):
        if left > right:
            return None
        mid = left + (right - left)//2
        root = TreeNode(nums[mid])
        root.left = self.helper(left, mid-1, nums)
        root.right = self.helper(mid+1, right, nums)
        return root
