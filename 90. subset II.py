# solution 2 - BFS
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)

        subsets = []
        subsets.append([])

        for n in range(len(nums)):
            start = 0
            if n > 0 and nums[n] == nums[n-1]:
                start = end
            end = len(subsets)
            for i in range(start, end):
                temp = list(subsets[i])
                temp.append(nums[n])
                subsets.append(temp)

        return subsets
        
    # solution 1 - DFS backtracking
    def subsetsWithDup(self, nums):
        self.res = []
        nums= sorted(nums) # sort arr so that duplicate numbers are put together
        self.dfs(nums, 0, [])
        return self.res

    def dfs(self, nums, start, path):
        self.res.append(path)

        for i in range(start, len(nums)):
            # skip duplicate number
            if i > start and nums[i] == nums[i-1]:
                continue
            # path.append(nums[i])
            self.dfs(nums, i+1, path + [nums[i]])
            # path.pop()
