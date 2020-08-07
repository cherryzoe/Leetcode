Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

解题思路：
- 滑动窗口， 
- 用字典记录窗口内每个字符出现的次数，记录当前的字符长度
- 一旦窗口新加进的元素 是窗口已有字符，从窗口左边开始一一剔除元素，直到重复字符个数重新回到1为止，

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        l = res = 0
        
        for i,v in enumerate(s):
            if v in dic:
                dic[v] += 1
            else:
                dic[v] = 1
            while dic[v] > 1 and l < i:
                dic[s[l]] -= 1
                l += 1
            res = max(res, i-l+1)
        
        return res
