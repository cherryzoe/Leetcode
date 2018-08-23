Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        stack = []
        num = 0
        sign = '+'
        for i in range(len(s)):
            # if s[i].isdigit():
            #     num = ord(s[i]) - ord('0')
            #     while i+1 < len(s) and s[i+1].isdigit():
            #         num = num * 10 + ord(s[i+1]) - ord('0')
            #         i += 1
                    
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
                
            if not s[i].isdigit() and s[i] != ' ' or i == len(s)-1:           
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    stack.append(stack.pop()*num)
                if sign == '/':
                    if stack[-1]//num < 0 and stack[-1] % num != 0:
                        stack.append(stack.pop()//num + 1)
                    else:
                        stack.append(stack.pop()//num)
                sign = s[i]
                num = 0
        return sum(stack)
            
             
        
