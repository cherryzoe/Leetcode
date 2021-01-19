给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
解题思路：
1. 回溯
2. 剪枝条件 - 将输入数组排序后，每次只从当前位置往右边递归，下一层的起始位置定位当前index，这样可以避免重复路径
遇到负值的直接停止下面的递归

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        self.res = []
        candidates = sorted(candidates)
        self.backtracking(candidates, 0, [], target)
        return self.res
    
    def backtracking(self, candidates, start, path, target):
        if target == 0:
            self.res.append(path)
            return
        
        for index in range(start, len(candidates)):
            if target - candidates[index] < 0:
                break
            self.backtracking(candidates, index, path + [candidates[index]], target-candidates[index])
            下一层的起始位置定位当前index，这样可以避免重复路径
        
