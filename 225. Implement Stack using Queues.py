# Implement the following operations of a stack using queues.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# Example:

# MyStack stack = new MyStack();

# stack.push(1);
# stack.push(2);  
# stack.top();   // returns 2
# stack.pop();   // returns 2
# stack.empty(); // returns false
# Notes:

# You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

# in python, collections.deque is the default way to implement queue data structure.
# De-queue: deque.popleft() is O(1) - pop from front
# En-queue: deque.append() - add from end

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        q = self.queue
        q.append(x)
        for i in range(len(q)-1):
            q.append(q.popleft())
#             everytime we push a new element into queque, we move out all exsiting element from queue(except new append) from head 
#             and append to the tail. in this way we make sure the new element push into queue will be the first one to pop out next time

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self.queue) > 0:
            return self.queue.popleft()
        return None
            

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
