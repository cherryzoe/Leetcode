# iven a string, sort it in decreasing order based on the frequency of characters.

# Example 1:

# Input:
# "tree"

# Output:
# "eert"

# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# 解题思路：
# 1.用字典记录每个字符出现次数
# 2.用tuple的形式将（char, cnt)加入到heap中，利用heap自动排序的特点，把个数和字符组成pair放到优先队列里排好序后，再取出来组成结果res即可

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        minHeap = []
        res = ''
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        for key, val in dic.items():
            heapq.heappush(minHeap, (val, key)) #heap会根据根据tuple中第一个元素val排序，小的在堆顶，大的往下排
        
        while minHeap:
            cnt, val = heapq.heappop(minHeap)
            temp = val * cnt
            res = temp + res 
        return res 
   
# 排序部分也可以不用heap，直接用排序函数，得到的结果是tuples(cha, cnt),如(a,1)(b,5)
        dic = sorted(dic.items(), key = lambda k:k[1])
        for item in dic:
            val, cnt = item[0], item[1]
            res = val * cnt + res
        return res
