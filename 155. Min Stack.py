# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.minStack) == 0 or x <= self.minStack[-1]:
            self.minStack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        if self.top() == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """        
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# reference: http://bangbingsyb.blogspot.com/2014/11/leetcode-min-stack.html 
# 思路：

# 看到题目第一反应是用一个int minVal来记录整个stack当前的最小值就可以了。然后仔细想下，发现问题在于当这个最小值被pop以后，无法O(1)时间得到新的最小值。所以问题的关键在于要跟踪记录每个新数字压入栈时的当前最小值，而不是只记录一个总的最小值。

# 一种思路是将make_pair(xi, curMin)一起压入栈stack<pair<int,int>>中。但这种方法的空间复杂度为2n。再仔细观察，发现只有当push或pop的对象xi<= min(stack)时，才会影响到min(stack)的值。

# 用另一个stack<int> trackMin来记录min值的变化，trackMin.top()表示当前最小值。
# 当有新的xi<=trackMin.top()被压入时，将xi压入trackMin变为新的当前最小值。
# 当xi==trackMin.top()时被pop出时，trackMin也同时pop。

# 这里的一个关键是理解为什么是x<=trackMin.top()而不是x<trackMin.top()。加入对于push(x)只有当x<trackMin.top()时，才将x压入trackMin中。

# 例如压入以下数后：
# xi:    3 2 1 2 1 
# trackMin: 3 2 1

# 此时如果pop，则变为
# xi:    3 2 1 2
# trackMin: 3 2

# 然而实际栈里的最小值仍旧为1，这个1因为重复数字的关系在trackMin中丢失
