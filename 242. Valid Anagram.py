# Given two strings s and t, write a function to determine if t is an anagram of s.

# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.

# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

solution1:(slowest)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n1 = collections.Counter(s)
        n2 = collections.Counter(t)
        return n1==n2

    
solution2:
#     It creates a size 26 int arrays as buckets for each letter in alphabet. 
#     It increments the bucket value with String s and decrement with string t. 
#     So if they are anagrams, all buckets should remain with initial value which is zero. 
#     So just checking that and return
        n = [0] * 26
        for i in s:
            n[ord(i) - ord('a')] += 1
        for j in t:
            n[ord(j) - ord('a')] -= 1
        for k in n:
            if k != 0:
                return False
        return True
    
solution3:(best) faster than sol2 and much faster than sol1
    class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lst = collections.defaultdict(int)
        for i in s:
            lst[i] += 1
            
        for j in t:
            if j not in lst:
                return False
            lst[j] -= 1
            if lst[j] == 0:
                del(lst[j])
        return len(lst) == 0
