 take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
             
1. 若字符串开头是空格，则跳过所有空格，到第一个非空格字符，如果没有，则返回0.
2. 若第一个非空格字符是符号 +/-，则标记 sign 的真假
3. 若下一个字符不是数字，则返回0，完全不考虑小数点和自然数的情况
4. 如果下一个字符是数字，则转为整形存下来，若接下来再有非数字出现，则返回目前的结果。
5. 还需要考虑边界问题，如果超过了整型数的范围，则用边界值替代当前值。

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res = 0
        sign = 1
        s = str.strip() #delete space in front
        if not len(s):
            return 0
        if s[0] in ['+','-']:
            if s[0] == '-':
                sign = -1
            else:
                sign = 1
            s = s[1:]
        for c in s:
            if c.isdigit():
                res = res * 10 + int(c)
            else:
                break
        res *= sign
        if res > 2**31-1: return 2**31-1
        if res < -2**31: return -2**31
        return res
