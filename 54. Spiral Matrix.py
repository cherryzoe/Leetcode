# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
# Example 1:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]


# https://www.cnblogs.com/zuoyuan/p/3769829.html

8/19/2020
思路： 
把第一个元素存到结果里，遍历矩阵，原则是站在前一个节点上，先判断，再移动
判断条件： 
1. 下一个节点是否越界  2.同时也没有遍历过 
值得注意的是每次调用matrix[][]都需要保证下表不越界。用&&【AND】的情况下，若条件1）x+1 < n 不满足，将不会计算matrix[][]，因此也不会出现下标越界的情况 
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res = [matrix[0][0]]
        matrix[0][0] = ''
        row, col = len(matrix), len(matrix[0])
        cnt = row * col - 1
        x, y = 0, 0
        
        while cnt > 0:
            while y+1 < col and matrix[x][y+1] != '':
                y += 1
                res.append(matrix[x][y])
                matrix[x][y] = ''
                cnt -= 1
            while x+1 < row and matrix[x+1][y] != '':
                x += 1
                res.append(matrix[x][y])
                matrix[x][y] = ''
                cnt -= 1
            while y-1 >= 0 and matrix[x][y-1] != '':
                y -= 1
                res.append(matrix[x][y])
                matrix[x][y] = ''
                cnt -= 1
            while x-1 >= 0 and matrix[x-1][y] != '':
                x -= 1
                res.append(matrix[x][y])
                matrix[x][y] = ''
                cnt -= 1
        return res

2018
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res
        left, right, up, down = 0, len(matrix[0])-1, 0, len(matrix)-1
        direct = 0 # 0: go right   1: go down  2: go left  3: go up
        while True:
            if direct == 0:
                for i in range(left, right+1):
                    res.append(matrix[up][i])
                up += 1
            if direct == 1:
                for i in range(up, down+1):
                    res.append(matrix[i][right])
                right -= 1
            if direct == 2:
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                down -= 1
            if direct == 3:
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
                left += 1
            if left > right or up > down:
                return res
            direct = (direct + 1)%4
