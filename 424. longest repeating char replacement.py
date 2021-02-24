给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。

注意：字符串长度 和 k 不会超过 104。


示例 1：

输入：s = "ABAB", k = 2
输出：4
解释：用两个'A'替换为两个'B',反之亦然。
示例 2：

输入：s = "AABABBA", k = 1
输出：4
解释：
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。

This problem follows the Sliding Window pattern, and we can use a similar dynamic sliding window strategy as discussed in No-repeat Substring. We can use a HashMap to count the frequency of each letter.

We’ll iterate through the string to add one letter at a time in the window.
We’ll also keep track of the count of the maximum repeating letter in any window (let’s call it maxRepeatLetterCount).
So, at any time, we know that we can have a window which has one letter repeating maxRepeatLetterCount times; this means we should try to replace the remaining letters.
If we have more than ‘k’ remaining letters, we should shrink the window as we are not allowed to replace more than ‘k’ letters.
While shrinking the window, we don’t need to update maxRepeatLetterCount (which makes it global count; hence, it is the maximum count for ANY window). 
Why don’t we need to update this count when we shrink the window? The answer: In any window, since we have to replace all the remaining letters to get the 
  longest substring having the same letter, we can’t get a better answer from any other window even though all occurrences of the letter with frequency
  maxRepeatLetterCount is not in the current window.

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        frequency = [0] * len(s)
        start = 0
        res = 0
        max_freq = 0

        for end in range(len(s)):
            end_s = s[end]
            index = ord(end_s) - ord('A')
            frequency[index] += 1
            max_freq = max(max_freq, frequency[index])
            # Current window size is from window_start to window_end, overall we have a letter which is
            # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
            # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
            # if the remaining letters are more than 'k', it is the time to shrink the window as we
            # are not allowed to replace more than 'k' letters
            while max_freq + k < end - start + 1:
                frequency[ord(s[start])-ord('A')] -= 1
                start += 1
            res = max(res, end-start+1)
        return res
