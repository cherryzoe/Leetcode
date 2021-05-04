# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

# 5/4/2021
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        lists = list(s)
        listp = list(p)
        res = []
        cntp = {}
        for i in listp:
            cntp[i] =  cntp.get(i,0) + 1

        left = 0
        cnt = {}
        for right in range(len(lists)):
            cur = lists[right]

            # skip to the next element if current not in target scope
            if cur not in cntp:
                left = right + 1
                cnt = {}
                continue

            cnt[cur] = cnt.get(cur, 0) + 1

            # pop out left elements unitl total# current element falls into target scope counts
            while cnt[cur] > cntp.get(cur,0):
                cnt[lists[left]] -= 1
                left += 1

            # As logn as there is extra elements, they are being popped out from previous steps, 
            # If elements in current window is exact target length, then it's anagrams of p
            if right - left + 1 == len(listp):
                res.append(left)
        return res 



#Sliding window solution. Add one element in right edge and discard one element in left edge, then compare
#If use another inner loop, with time exceed limit
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ls, lp = len(s), len(p)
        res = []
        i = lp
        cp, cs = collections.Counter(p), collections.Counter(s[:i])
        if cp == cs:
            res.append(0)
        for i in range(lp, ls):
            cs[s[i]] += 1
            cs[s[i-lp]] -= 1
            # when compare Counter, {a:0,b:1} is different with {b:0}. so we need to delete enpty elements to avoid miscompare
            if cs[s[i-lp]] == 0:
                del cs[s[i-lp]]
            if cs == cp:
                res.append(i-lp+1)
        return res
