Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:

Input: s = "a", t = "a"
Output: "a"

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        # sliding window
        # expand window size until we include all target elements and each of their counts is no less than target
        # record as one of possible result and start to pop elements from the left, stops popping if we hit the target element and its count is 0 (0 means its count just makes the correct)

        dic = {}
        for i in t:
            dic[i] = dic.get(i,0) + 1
        cnt = len(t)
        min_len = sys.maxsize
        res = ''
        
        left = 0
        for right in range(len(s)):
            # extend right boarder
            cur = s[right]
            if dic.get(cur, 0) > 0:
                cnt -= 1
            dic[cur] = dic.get(cur, 0) - 1

            while cnt == 0:
                # update result
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left: right+1]
                # pop left element one by one unitl it no longer contians all valid elements/that is when cnt < 0
                pre = s[left]
                if dic.get(pre, 0) == 0:
                    cnt += 1
                dic[pre] = dic.get(pre, 0) + 1
                left += 1
                    
        return res
