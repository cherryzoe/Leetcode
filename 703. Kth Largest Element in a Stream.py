Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Returns the element representing the kth largest element in the stream.
 

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

解题思路：
用priority queue，Python中是heapq.heap的大小维持为K，这样堆顶heap[0]总是堆中所有元素中最小的，第K大元素，堆里的元素就是前K大的集合。
遍历nums过程中把每一个val跟堆顶元素比，如果比堆顶元素大，那说明val应该加入堆而现有堆顶元素要被踢出。

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.pq = [] 
        self.k = k
        for n in nums:
            self.add(n)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.pq) < self.k:
            heappush(self.pq, val)
        else:
            top = self.pq[0]
            if val > top:
                heappop(self.pq)
                heappush(self.pq, val)
        return self.pq[0]
      

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
