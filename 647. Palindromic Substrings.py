# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# Note:
# The input string length won't exceed 1000.

# idea: Step 1: Start a for loop to point at every single character from where we will trace the palindrome string.
# checkPalindrome(s,i,i); //To check the palindrome of odd length palindromic sub-string
# checkPalindrome(s,i,i+1); //To check the palindrome of even length palindromic sub-string

# Step 2: From each character of the string, we will keep checking if the sub-string is a palindrome and increment the palindrome count. 
# To check the palindrome, keep checking the left and right of the character if it is same or not.

class Solution(object):
    
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.cnt = 0
        for i in range(len(s)):
            self.check(s, i, i)
            self.check(s, i, i+1)
        return self.cnt
        
    def check(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            self.cnt += 1
            left -= 1
            right += 1  
