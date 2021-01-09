Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

解题思路：
用 row 9*{} col 9*{} cube 3*3*{}分别记录每一行每一列以及每一块出现过的数字。
两层循环遍历整个棋盘，同时在行列cube中检查这个数是否已经出现过，如出现过则返回false。不然就存进去。
难点在于cube的表示，比如说board[5][1]，应该落到cube[1][0]中，相应的处理是 5/3 -> 1, 1/3 -> 0
00 01 02
10 11 12
20 21 22

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [set() for i in range(len(board))]
        col = [set() for i in range(len(board))]
        cube = [[set() for i in range(len(board))] for j in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board)):
                
                curNode = board[i][j]
                if curNode == '.':
                    continue
                cur = int(curNode)
                
                if cur in row[i] or cur in col[j] or cur in cube[i//3][j//3]:
                    return False
                
                row[i].add(cur)
                col[j].add(cur)
                cube[i//3][j//3].add(cur)
        return True
