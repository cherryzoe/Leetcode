# Write a function that takes a string as input and returns the string reversed.

# Example:
# Given s = "hello", return "olleh".

# solution 1: （比第二种解法慢很多）
def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = list(s)
        for i in range(len(n)/2):
            temp = n[i]
            n[i] = n[len(n)-i-1]
            n[len(n)-i-1] = temp
        return ''.join(n)
        
#  solution 2:
 def reverseString(self, s):    
      return s[::-1]
