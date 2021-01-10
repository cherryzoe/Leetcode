编写一个程序，通过填充空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。

解题思路：
跟N皇后问题是一类
先扫描一遍棋盘，把预设值都记录到全局变量row, col, cube中。
用回溯方法，一个个试下去，如果一条路走到底，层层返回TRUE，那么就是答案，直接返回。 
否则任何一层False，然后回到上一层，移除row, col, cube中的记录，并且棋盘重置成空，恢复现场

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
    
        self.row = [set() for _ in range(9)]
        self.col = [set() for _ in range(9)]
        self.cube = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if  cur != '.':
                    self.row[i].add(int(cur))
                    self.col[j].add(int(cur))
                    self.cube[i//3][j//3].add(int(cur))
   
        self.backtracking(board)
  

    def backtracking(self, board):

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    continue
                
                for n in range(1,10):
                    if n in self.row[i] or n in self.col[j] or n in self.cube[i//3][j//3]:
                        continue
                    self.row[i].add(n)
                    self.col[j].add(n)
                    self.cube[i//3][j//3].add(n)

                    board[i][j] = str(n)

                    if self.backtracking(board):
                        return True
                    
                    self.row[i].remove(n)
                    self.col[j].remove(n)
                    self.cube[i//3][j//3].remove(n)
                    
                    board[i][j] = '.'

                return False
        return True

