# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for string in strs:
            dic[''.join(sorted(string))].append(string)
            
        return list(dic.values())


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
            key = ''.join(sorted(s))
            # or we can use: key  = tuple(sorted(s)). list can not be the key of dictionary. need to converti list to string or tuple
            if key not in dic:
                dic[key] = [s]
            else:
                dic[key] += [s]
        return dic.values()
