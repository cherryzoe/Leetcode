# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

# Example:

# Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Output: 
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]

# create a dictinary to store: key = offset(char[i] - char[0]), value = List(strings with same key)
# we get defaultdict(<type 'list'>, {(0, 1, 2): [u'abc', u'bcd', u'xyz'], (0, 2, 4, 5): [u'acef'], (0,): [u'a', u'z'], (0, 25): [u'az', u'ba']})

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        groups = collections.defaultdict(list)
        for s in strings:
            groups[tuple((ord(c) - ord(s[0])) % 26 for c in s)] += s,
            # %26 to deal with [az, ba]. ','is necessary when using '+' to append to list: += something,
        return groups.values()
