# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        div = 1
        n = x
        while n >= 10:
            div *= 10
            n /= 10

        #注意此处一定是大于0， 对于处理后只剩一位数的情况，有两种可能：
        # 1. 121 一个循环后，去除left 和 right位置的1， 只剩中间的2. 2/div判断是否有left 和 right。 此种条件下left = right
        # 2. 1021 在一个循环后， 得到2但实际上得到的是02，这种情况通过 除以div（10)可得出left=0， right = 2， left !=right
        while x > 0:
            
            left = x / div
            right = x % 10
            if left != right:
                return False
            x = (x - left*div)/10
            div /= 100
        return True
