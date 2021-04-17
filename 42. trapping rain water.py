class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        stack = []
        res = 0
        # 维护一个严格单调递减的栈。当需要往里面加入新元素时，与栈顶（当前栈中的最小元素）比较，若cur大于或者等于栈顶元素，将栈顶元素pop出来，与下一个栈顶元素继续比较。
        # 每pop出一个比cur小的栈顶元素，res加上栈顶元素跟其小一点的之前栈顶元素的差值就是其储水高度，栈顶元素坐标距离cur的距离-1就是储水宽度，面积就是两者乘积
        
        #比如当前cur，比栈顶元素大，那么可以把cur当做是高墙，蓄水高度则取决于矮的一方与其底部的差值，蓄水宽度则是矮的一方到高墙的距离
        for i in range(len(height)):
            lastHeight = 0
            cur = height[i]
            while stack and cur >= height[stack[-1]]:
                res += (height[stack[-1]] - lastHeight) * (i - stack[-1]- 1)
                lastHeight = height[stack[-1]]
                stack.pop()
                
        # 当所有小于cur的栈顶元素都被pop出来以后，此时如果栈中还有元素就是比cur大的元素了，此时的栈顶是高墙，而cur变成矮的一方
        # cur 与 cur前一个栈顶高度之差 - 储水高度，cur与当前栈顶的距离 - 储水宽度。两者相乘，加入结果之后，再将cur放入栈中
            if stack:
                res += (cur - lastHeight) * (i - stack[-1] - 1)
            stack.append(i)
        return res
