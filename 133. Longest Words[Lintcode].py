# Given a dictionary, find all of the longest words in the dictionary.

# Example
# Given

# {
#   "dog",
#   "google",
#   "facebook",
#   "internationalization",
#   "blabla"
# }
# the longest words are(is) ["internationalization"].

# Given

# {
#   "like",
#   "love",
#   "hate",
#   "yes"
# }
# the longest words are ["like", "love", "hate"].

  def longestWords(self, dictionary):
        # write your code here
        longest = 0
        res = []
        dic = {n : len(n) for n in dictionary}
        for i,v in dic.items():
            longest = max(longest, v)
        res = [x for x,y in dic.items() if y == longest]
        return res
