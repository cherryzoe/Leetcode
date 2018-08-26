Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


solution1: Iteration

我们可以一位一位的网上叠加，比如对于题目中给的例子[1,2,3]来说，最开始是空集，那么我们现在要处理1，就在空集上加1，为[1]，
现在我们有两个自己[]和[1]，下面我们来处理2，我们在之前的子集基础上，每个都加个2，可以分别得到[2]，[1, 2]，
那么现在所有的子集合为[], [1], [2], [1, 2]，同理处理3的情况可得[3], [1, 3], [2, 3], [1, 2, 3], 
再加上之前的子集就是所有的子集合了

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subs = [[]]
        nums = sorted(nums)
        for i in range(len(nums)):
            for j in range(len(subs)):
                subs.append(subs[j] + [nums[i]])
        return subs
           
           
 solution2: Recursive
 下面来看递归的解法，相当于一种深度优先搜索，参见网友JustDoIt的博客，由于原集合每一个数字只有两种状态，要么存在，要么不存在，那么在构造子集时就有选择和不选择两种情况，
 所以可以构造一棵二叉树，左子树表示选择该层处理的节点，右子树表示不选择，最终的叶节点就是所有子集合，树的结构如下：
                        []        
                   /          \        
                  /            \     
                 /              \
              [1]                []
           /       \           /    \
          /         \         /      \        
       [1 2]       [1]       [2]     []
      /     \     /   \     /   \    / \
  [1 2 3] [1 2] [1 3] [1] [2 3] [2] [3] []
  
 class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) == 0:
            return []
        self.helper(sorted(nums), 0, [], res)
        return res
        
    def helper(self, nums, indx, subset, res):
        res.append(subset)
        
        for i in range(indx, len(nums)):
            subset = subset + [nums[i]]
            self.helper(nums, i+1, subset, res)
            subset = subset[:-1]
        
       
                
  
       
                
