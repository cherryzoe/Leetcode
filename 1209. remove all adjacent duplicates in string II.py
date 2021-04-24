class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # 用栈来存[s, cnt]。
        # 每次入栈的元素跟栈顶元素比较，不同直接入栈
        # 如果相同，进一步比较 - 若加上当前的个数等于K，则弹出栈（删除）， 否则增加栈顶元素的cnt。 
        stack = []
        res = ''
        for string in s:
            if stack and string == stack[-1][0]:
                if stack[-1][1] < k-1:
                    stack[-1][1] += 1
                else:
                    stack.pop()
            else:
                stack.append([string, 1])
        for i in stack:
            char, cnt = i[0], i[1]
            res += char * cnt
        return res
