给定一个字符串，逐个翻转字符串中的每个单词。

示例：

输入: ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
输出: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
注意：

单词的定义是不包含空格的一系列字符
输入字符串中不会包含前置或尾随的空格
单词与单词之间永远是以单个空格隔开的
进阶：使用 O(1) 额外空间复杂度的原地解法。

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i,j = 0,1
        self.reverse(s, 0, len(s)-1)
        while j < len(s):
            # j 停止在空字符串处或者是s的末尾
            while j < len(s) and s[j] != ' ':
                j += 1
            self.reverse(s, i, j-1)
            j += 1
            i = j
         

    def reverse(self, s, i , j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
