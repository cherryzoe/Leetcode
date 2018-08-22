Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Consider the following binary search tree: 

     5
    / \
   2   6
  / \
 1   3
Example 1:

Input: [5,2,6,1,3]
Output: false
Example 2:

Input: [5,2,1,3,6]
Output: true
Follow up:
Could you do it using only constant space complexity?

class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if not preorder:
            return True
        return self.helper(preorder)
    
    def helper(self, nums):
        if not nums or len(nums) == 1:
            return True
        size = len(nums)
        index = size
        root = nums[0]
        for i in range(1, size):
            if nums[i] > root: 
                index = i   
                break       
        if index != -1:     
            for x in range(index, size):
                if nums[x] < root:
                    return False
        if index == size:
            return self.helper(nums[1:index])      
        else:
             return self.helper(nums[1:index]) and self.helper(nums[index: ])255. Verify Preorder Sequence in Binary Search Tree
