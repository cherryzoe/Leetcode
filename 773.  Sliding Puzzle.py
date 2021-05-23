class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        # """
        # convert board(2 D matrix) into string-1 dimension easier to compare
        # BFS from start node to target
        # matrix(i,j) -> str(index = i*3 + j)

        res = 0
        start = self.toString(board)
        target ='123450'
        q = collections.deque([start])
        visited = set([start])

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return res
                for nex in self.getNext(cur):
                    if nex not in visited:
                        visited.add(nex)
                        q.append(nex)
            res += 1
        return -1

    def toString(self, board):
        res = ''
        for i in range(2):
            for j in range(3):
                res = res + str(board[i][j])
        return res 

    def getNext(self, cur):
        res = []

        idx_zero = cur.index('0')
        x = idx_zero // 3 # map index of string to matrix(x,y)
        y = idx_zero % 3 
        
        # get the elements around 0 in 4 directions
        dx, dy = [0,0,1,-1], [1,-1,0,0]
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]

            if x_ < 0 or x_ > 1 or y_ < 0 or y_ > 2:
                continue

            idx_nex = x_ * 3 + y_
            temp = list(cur) # string immutable, list mutable
            # swap the elements with 0
            temp[idx_nex], temp[idx_zero] = temp[idx_zero], temp[idx_nex] 
            res.append(''.join(temp)) # list -> string
        return res



