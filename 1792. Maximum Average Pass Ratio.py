
# 判断每个班级的潜力值 = 加上一个优等生后的通过率-现在的通过率
# 用最小堆存放 （潜力值（负值），x,y)，每次取出的堆顶元素，即潜力最大的班级，给他分配一个优等生，重新计算潜力值，再重新加入堆中
class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        import heapq
        ratings = []
        n = len(classes)

        for x, y in classes:
            r = x/ float(y) - (x+1.) / (y+1.) 
            heappush(ratings, (r, x, y))

        for _ in range(extraStudents):
            r, x, y = heappop(ratings)
            x += 1.
            y += 1.
            r = x/ float(y) - (x+1.) / (y+1.) 
            heappush(ratings, (r, x, y))
        
        res = 0.
        for _, x, y in ratings:
            res += x/float(y)
        return res/n
