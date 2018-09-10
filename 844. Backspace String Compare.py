# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

# Example 1:

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:

# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:

# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:

# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# Note:

# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# Follow up:

# Can you solve it in O(N) time and O(1) space?

# solution1: with extra O(n) space
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.tostring(S) == self.tostring(T)
    
    def tostring(self, string):
        stack = []
        for s in string:
            if s == '#':
                stack = stack[:-1]
            else:
                stack.append(s)
        return ''.join(stack)
        
# solution2: O(1)space?
#     Iterate through the string in reverse. If we see a backspace character, the next non-backspace character is skipped. 
#     If a character isn't skipped, it is part of the final answer.
    class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.tostring(S) == self.tostring(T)
    
    def tostring(self, string):
        skip = 0
        res = []
        for s in reversed(string):
            if s == '#':
                skip += 1
            else:
                if skip:
                    skip -= 1
                else:
                    res.append(s)
        return ''.join(res)
        
        
