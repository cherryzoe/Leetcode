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

    imporoved solution - bidirectional BFS
    class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        dirs = [ [1, 2], [1,-2],[-1,2], [-1, -2], [2, 1], [2, -1], [-2, -1], [-2, 1]]        
        x, y = abs(x), abs(y) # reduce 4 section into only check 1st section
      
        visited_A = set()
        q_A = collections.deque()
        q_A.append((0,0))
        visited_A.add((0,0))
        q_B = collections.deque()
        q_B.append((x, y))
        visited_B = set()
        visited_B.add((x,y))

        cnt = 0
        while q_A and q_B:
            if len(q_A) > len(q_B):
                q_A, q_B = q_B, q_A
                visited_A, visited_B = visited_B, visited_A

            n = len(q_A)
            for _ in range(n):  
                cx, cy = q_A.popleft()
                # if current node has been visited by B, that means path A-B exisits and cur is the connecting point
                if (cx, cy) in visited_B:
                    return cnt
                for d in dirs:
                    dx, dy = d[0], d[1]
                    nx, ny = cx+dx, cy+dy
                    # 新的点如果是离目标越走越远，则不考虑
                    if (nx,ny) not in visited_A:
                        #  and math.sqrt((nx-x)**2 + (ny-y)**2) <= math.sqrt((cx-x)**2 + (cy-y)**2)+10:
                        visited_A.add((nx,ny))
                        q_A.append((nx,ny))
            cnt += 1
        return -1
