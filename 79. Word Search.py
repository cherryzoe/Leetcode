# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
#         数组中每一个点都可能是有效字符串的起点， 只要找到任意就表示有解
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, 0, i, j):
                    return True
        return False
       
        
    def dfs(self, board, word, idx, row, col):
        if idx == len(word):
            return True
#           出界条件要先判断，否则在下一步调用数组【i][j]时有index out range的错误
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False
        
        if board[row][col] != word[idx] or self.visited[row][col] == True:
            return False
        
        self.visited[row][col] = True
        
        if self.dfs(board, word, idx + 1, row + 1, col):
            return True

        if self.dfs(board, word, idx + 1, row - 1, col):
            return True
        
        if self.dfs(board, word, idx + 1, row, col + 1):
            return True
        
        if self.dfs(board, word, idx + 1, row, col - 1):
            return True
#         回溯，将改点重新改回unvisited， 意思是当前的点并未成功作为有效字符串解，因此下次还有机会被使用
        self.visited[row][col] =  False
        
        return False
