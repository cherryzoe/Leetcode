Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.


solution 1: BFS
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        level = {beginWord:1}
        queue = collections.deque([beginWord])
        
        while queue:
            word = queue.popleft()
            if  word == endWord:
                return level[word]  
            
            next_words = self.get_next_word(word)
            for next_word in next_words:
                if next_word in level or next_word not in wordList:
                    continue
                level[next_word] = level[word] + 1
                queue.append(next_word)
        return 0
        
        
    def get_next_word(self, word):
        words = []
        for i in range(len(word)):
            left = word[:i]
            right = word[i+1:]
            for cur in 'abcdefghijklmnopqrstpqrstuvwxyz':
                if cur == i:
                    continue
                words.append(left+cur+right)        
        
        return words
