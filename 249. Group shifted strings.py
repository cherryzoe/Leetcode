class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        # 将所有字符串转化成以a开头，存到hashmap中，映射关系为 转化后： 【转化前1，转化前2】
        # 同一字符串中的字符偏移量是相同的
        dic = {}
        for string in strings:
            off_set = ord(string[0]) - ord('a')
            temp = ''
            for s in string:
                temp += chr((ord(s) - off_set)%26)
            if temp not in dic:
                dic[temp] = [string]
            else:
                dic[temp].append(string)
        return  [i for i in dic.values()]
