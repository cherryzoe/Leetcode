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

# 4/21/2021
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[False] * len(s) for _ in range(len(s))]
        cnt = 0
        for i in range(len(s)):
            for j in range(i+1):
                # i j 重合，一个字符时‘a'这种情况是回文
                if i==j:
                    dp[j][i] = True 
                    cnt += 1
                # aa这种情况
                elif i-j == 1 and s[i] == s[j]:
                    dp[j][i] = True
                    cnt += 1
                else:
                # a-bcb-a这种情况
                    # i-j中间有2个以上字符时，当两头字符相同且剩下中间部分也为回文时，i-j为回文
                    if s[i] == s[j] and dp[j+1][i-1]: 
                        dp[j][i] = True
                        cnt += 1
        return cnt
    

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
            self.check(s, i, i) #To check the palindrome of odd length palindromic sub-string
            self.check(s, i, i+1) #To check the palindrome of even length palindromic sub-string
        return self.cnt
        
    def check(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            self.cnt += 1
            left -= 1 #To trace string in left direction
            right += 1   
