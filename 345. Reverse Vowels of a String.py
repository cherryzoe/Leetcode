# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:
# Given s = "hello", return "holle".

# Example 2:
# Given s = "leetcode", return "leotcede".

# Note:
# The vowels does not include the letter "y".


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls = list(s)
        left = 0
        right = len(ls) - 1
        v = ['a','o','e','i','u','A','O','E','I','U']
        while left < right:
            if ls[left] in v and ls[right] in v:
                ls[left], ls[right] = ls[right], ls[left]
                left += 1
                right -= 1
            else:
                if ls[left] not in v:
                    left += 1
                elif ls[right] not in v:
                    right -= 1
        return ''.join(ls)

    
# solution 2:
    while left < right:
    while s[left] not in v:
        left += 1
    while s[right] not in v:
        right -= 1
    s[left],s[right] = s[right], s[left]
    left += 1
    right -= 1
print s
