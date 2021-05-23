class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        # start = str(0000)
        # | level 1 [inc: 0001,0010,0100,1000, dec: 9000, 0900, 0090, 0009]
        # || level 2 [0002, 0011,1001, 0011 ...]
        # end = target
        # middle not in deadends

        deadends = set(deadends)
        start = '0000'
        if target == start:
            return 0
        if start in deadends: #if start position in deadends, there is no way to go
            return -1
        res = 0
        q = collections.deque([start])
        visited = set([start])

        while q:
            # print q
            n = len(q)
            for _ in range(n):
                cur = q.popleft()
                if cur == target:
                    return res 
                for nex in self.getNext(cur, deadends):
                    if nex not in visited:
                        visited.add(nex)
                        q.append(nex)
            res += 1
        return -1

    def getNext(self, cur, deadends):
        temp = []
        for i in range(len(cur)):
            x = (int(cur[i]) + 1) % 10
            nex = cur[:i] + str(x) + cur[i+1:]
            if nex not in deadends:
                temp.append(nex)

        for i in range(len(cur)):
            x = (int(cur[i]) - 1 + 10)%10
            nex = cur[:i] + str(x) + cur[i+1:]
            if nex not in deadends:
                temp.append(nex)

        return temp
