# The count-and-say sequence is the sequence of integers with the first five terms as following:

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth term of the count-and-say sequence.

# Note: Each term of the sequence of integers will be represented as a string.

# Example 1:

# Input: 1
# Output: "1"
# Example 2:

# Input: 4
# Output: "1211"

# 思路： 
# 设s[0]为baseline, 遍历s每一位字符，每个字符有且仅有两种可能性：
#  - 若与baseline相同，cnt加1. 继续到下一个字符
#  - 与baseline不同，将之前的结果以cnt + baseline 的格式存入temp中。同时将新字符设为basliene, cnt = 1，继续到下一个字符 
#  直到所有字符都结束时， 将剩余结果存入temp中。
# 将temp的值赋予s作为下次遍历的新字符串

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
    
        s = '1'
        for i in range(n-1):
            cnt, temp, baseline  = 0, '', s[0]
            for j in s:
                if j == baseline:
                    cnt += 1
                else:
                    temp += str(cnt) + baseline
                    baseline = j
                    cnt = 1
            temp += str(cnt) + baseline
            s = temp
        return s
            
            
