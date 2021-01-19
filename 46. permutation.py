给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []
        visited = []
        self.backtracking(visited, 0, nums, path, res)
        return res
    
    def backtracking(self, visited, start, nums, path, res):
        if len(path) == len(nums):
            res.append(path)
            return 
        
        for i in range(start, len(nums)):
            if nums[i] in visited:
                continue
            # self.visited.append(nums[i]) 
            # 如果用全局变量visited时候需要添加和移除恢复现场，如果作为参数传到下一层就不需要，
            # 记得visited+[nums[i]]一定要写在参数位置上，而不可以在for循环中
            self.backtracking(visited+[nums[i]], start, nums, path + [nums[i]], res)
            # self.visited.pop()
            
