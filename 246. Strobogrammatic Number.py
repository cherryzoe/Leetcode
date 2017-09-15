# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Write a function to determine if a number is strobogrammatic. The number is represented as a string.

# For example, the numbers "69", "88", and "818" are all strobogrammatic.

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dic = {'0':'0', '1':'1', '6':'9', '9':'6', '8':'8'}
        for i in range(len(num)/2+1):
            if dic.get(num[i]) != num[-1-i]:
                return False
        return True
            
