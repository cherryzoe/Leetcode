# Given a nested list of integers, implement an iterator to flatten it.

# Each element is either an integer, or a list -- whose elements may also be integers or other lists.

# Example 1:
# Given the list [[1,1],2,[1,1]],

# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

# Example 2:
# Given the list [1,[4,[6]]],

# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
# 与Flatten List类似，但是那道题用递归的方式，而这道题要求用迭代的方式。
# 迭代可以利用stack来完成。先将list中所有元素从后往前压入栈中。在hasNext()中，首先判断栈是否为空，若不为空再判断栈顶元素是整数还是list，
# 若是整数则返回true，若是list则移除栈顶元素，并将其中元素按从后往前压入栈中，并再次从头执行hasNext的步骤，
# 直到栈为空则返回false。next则直接取出栈顶元素并返回其值（根据hasNext，一定为整数而非list）。
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]
        
    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()
        
    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + (top.getList()[::-1])
        return False
# wrong solution as following, here get [] result, don't know why:
        def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            node = self.stack.pop()
            self.stack = self.stack.append(node.getList()[::-1])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
