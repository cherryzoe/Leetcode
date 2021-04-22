class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # check if can make palindrome - a most of one odd number of letter
        self.counts = collections.Counter(s)
        odd = ''
        odd_cnt = 0
        for string, c in self.counts.items():
            if c % 2 == 1:
                odd_cnt += 1
                odd = string
        if odd_cnt > 1:
            return []
        
        self.res = []
        if odd != '':
            self.counts[odd] -= 1
        # 奇数个的字符，取一个放在中间。如没有奇数个字符，odd保持初始值‘’
        self.dfs(s, odd)
        return self.res 

    def dfs(self, s, path):
        
        if len(path) == len(s):
            self.res.append(path)
            return 

        # 回溯
        for char, cnt in self.counts.items():
            if cnt > 0:
                self.counts[char] -= 2
                self.dfs(s, char + path + char)
                self.counts[char] += 2

