# Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

 

# Example 1:

# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
# Example 2:

# Input: matrix = [[-5]], k = 1
# Output: -5

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        # 最小堆 - 每行列首元素为此行最小元素，由每行列首组成一个候选列，
        # 第一列元素入堆，值和位置都录入，每次从堆里弹出最小值，通过其坐标，找到其右边（下一个）元素，继续入堆
        # 第k次弹出的即第K小元素
        minHeap = []
        row = len(matrix)
        col = len(matrix[0])
        # heappush take 2 parameter, make the second as tuple if there is mulitple
        for i in range(row):
            heapq.heappush(minHeap, (matrix[i][0], i, 0))
        
        while minHeap and k:
            n, x, y = heapq.heappop(minHeap)
            if y < col-1:
                heapq.heappush(minHeap, (matrix[x][y+1], x, y+1))
            k -= 1
        # 出while循环是k减到0的情况，最后一次弹出的就是第k小的元素
        return n
            

            



    
