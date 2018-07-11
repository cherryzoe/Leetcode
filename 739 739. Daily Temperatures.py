Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        size = len(temperatures)
        res =[0] * size
        for i in range(size - 1, -1, -1):
            j = i + 1
            while j < size and temperatures[j] <= temperatures[i]:
                if res[j]:
                    j = res[j] + j
                else:
                    j = size
            if j < size:
                res[i] = j -i
        return res
