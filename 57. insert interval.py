给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1：

输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
示例 2：

输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        left, right = newInterval
        i = 0 
        while i < len(intervals):
            # 当插入区间与当前区间没有重合时
            if intervals[i][1] < left or intervals[i][0] > right:
                res.append(intervals[i])
            else:
                # 当插入区间与当前区间有重合时 when intervals[i][0] in newInterval or intervals[i][1] in newInterval:
                left = min(intervals[i][0], left)
                right = max(intervals[i][1],right)
            i += 1
        res.append([left, right]) #当所有left 和 right 都更新完毕后，加入答案
        return sorted(res)
