
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3



class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.cur = collections.deque(maxlen=size)
        self.cur_sum = 0.0 #initilize the variable as float
        self.maxsize = size
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """        
        if len(self.cur) >= self.maxsize:
            head = self.cur.popleft()
        else:
            head = 0
        self.cur_sum = self.cur_sum + val - head
        self.cur.append(val)
        return self.cur_sum/len(self.cur)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
