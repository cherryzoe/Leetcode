Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res =[]
        set1,set2,set3 = set('qwertyuiop'),set('asdfghjkl'),set('zxcvbnm')
        for word in words:
            lowerWord = set(word.lower())
            if lowerWord.issubset(set1) or lowerWord.issubset(set2) or lowerWord.issubset(set3):
                res.append(word)
        return res
        
