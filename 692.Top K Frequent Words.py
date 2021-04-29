# Given a non-empty list of words, return the k most frequent elements.

# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.
    
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        # """
        # hashmap统计每个单词频次，保存为word:cnt的格式
        # 通过排序，首先按照频次cnt降序排，同频的再根据其字母排 key = lambda k: (-k[1], k[0])
        
        # dic = {}
        # for word in words:
        #     dic[word] = dic.get(word, 0) + 1
        
        dic = collections.Counter(words)
        dic = sorted(dic.items(), key = lambda k: (-k[1], k[0]))
        return [key for key,val in dic[:k]]
