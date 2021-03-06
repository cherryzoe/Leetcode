# Implement the following operations of a queue using stacks.

# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# Example:

# MyQueue queue = new MyQueue();

# queue.push(1);
# queue.push(2);  
# queue.peek();  // returns 1
# queue.pop();   // returns 1
# queue.empty(); // returns false
# Notes:

# You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

# 思路： 
# move(): 当stack2为空，而stack1中存有元素时，将1中元素弹出并存入2以实现倒序排列
# 只有当要pop() peek()操作之前需要以上move()步骤

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.move()
        return self.stack2.pop()
      

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.move()
        return self.stack2[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack1 and not self.stack2

    def move(self):
        if not self.stack2:
            while self.stack1:
                x = self.stack1.pop()
                self.stack2.append(x)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
