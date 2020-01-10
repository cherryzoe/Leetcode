# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output: 5

# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# Example 2:

# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# Output: 0

# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.


# solution 1: BFS 
# Note: 务必将给定的wordList转成字典/SET，再查询，可大大降低查询速度

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        dic = set(wordList)
        visited = {beginWord:1}
        queue = collections.deque([beginWord])
        
        while queue:
            word = queue.popleft()
            if word == endWord:
                return visited[word]
            next_words = self.findAllNeghbers(word)
            for next_word in next_words:
                if next_word in visited or next_word not in dic:
                    continue
                queue.append(next_word)
                visited[next_word] = visited[word] + 1
        return 0
        
    
    def findAllNeghbers(self, word):
            neighbers = []
            for i in range(len(word)):
                left = word[:i]
                right = word[i+1:]
                for cur in 'qwertyuiopasdfghjklzxcvbnm':
                    if cur == word[i]:
                        continue
                    neighbers.append(left+cur+right)
            return neighbers
