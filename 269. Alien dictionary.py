There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.
 
Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

  # create a graph and maintain each node's in_degree
  # according to zero degree nodes, find their next nodes and keep tack of them in result
  # if there is cycle in graph, we are not able to pop out all nodes, in this case return ''

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # create a graph and maintain each node's in_degree
        # according to zero degree nodes, find their next nodes and keep tack of them in result
        # if there is cycle in graph, we are not able to pop out all nodes, in this case return ''

        graph = {}
        
        # initiate graph and create nodes
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = []
        # record orders in graph
        for i in range(1, len(words)):
            # for j in range(i, len(words)):
            word1 = words[i-1]
            word2 = words[i]
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return ''

            n = min(len(word1), len(word2))
            for k in range(n):
                if word1[k] != word2[k]:
                    graph[word1[k]].append(word2[k])
                    break
        # print graph

        # populate incoming degrees
        degree = {k: 0 for k in graph.keys()}
        
        for value in graph.values():
            for v in value:
                degree[v] += 1
        # print degree

        zero = collections.deque([k for k in degree if degree[k] == 0])
        res = collections.deque()

        while zero:
            node = zero.popleft()
            res.append(node)
            for nexts in graph[node]:
                for next in nexts:
                    degree[next] -= 1
                    if degree[next] == 0:
                        zero.append(next)
            # print res
       
        # cycle exist -  find invalid relation   
        if len(res) != len(graph):
            return ''

        return ''.join(res)
