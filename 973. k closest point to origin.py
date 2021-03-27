
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].



class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        minHeap = []
        res = []
        for p in points:
            distance = sqrt(p[0]*p[0] + p[1]*p[1])
            
            if len(minHeap) < k:
                heappush(minHeap, (-distance, p))
            else:
                max_distance, node = minHeap[0]
                if distance < abs(max_distance):
                    heappop(minHeap)
                    heappush(minHeap, (-distance, p))
                
        while minHeap:
            d, p = heappop(minHeap)
            res.append(p)
        return res


