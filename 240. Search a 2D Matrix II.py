# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Example:

# Consider the following matrix:

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.

# Given target = 20, return false.

Tips:
    We start search the matrix from top right corner, initialize the current position to top right corner, 
    if the target is greater than the value in current position, then the target can not be in entire row of current position because the row is sorted, if the target is less than the value in current position, then the target can not in the entire column because the column is sorted too. 
    We can rule out one row or one column each time, so the time complexity is O(m+n).


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False 

        row, col = 0, len(matrix[0])-1
        while col >= 0 and row < len(matrix):
            if target == matrix[row][col]:
                return True
            if target > matrix[row][col]:
                row += 1
            else:
                col -= 1
        return False
