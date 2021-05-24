class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # dirs = []
        # bfs: start = [0,0]   ->  target = [x,y]

        dirs = [ [1, 2], [1,-2],[-1,2], [-1, -2], [2, 1], [2, -1], [-2, -1], [-2, 1]]
        visited = set()
        q = collections.deque()
        q.append((0,0))
        visited.add((0,0))
        cnt = 0

        while q:
            n = len(q)
            for _ in range(n):  
                cx, cy = q.popleft()
                # print (cx,cy), cnt, q
                if cx == x and cy == y:
                    return cnt
                for d in dirs:
                    dx, dy = d[0], d[1]
                    nx, ny = cx+dx, cy+dy
                    # 新的点如果是离目标越走越远，则不考虑
                    if (nx,ny) not in visited and math.sqrt((nx-x)**2 + (ny-y)**2) <= math.sqrt((cx-x)**2 + (cy-y)**2)+10:
                        visited.add((nx,ny))
                        q.append((nx,ny))
            cnt += 1
        return -1
