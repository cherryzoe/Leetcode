Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        d1 = d2 = res = len(words)      
        for idx,word in enumerate(words,1):
            if word == word1:
                d1 = idx
                res = min(res, abs(d1-d2))
            if word == word2:
                d2 = idx
                res = min(res, abs(d1-d2))
        return res
            
