
# 比如输入logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# 依据id后的第一个元素分类得到两类：
# letters = ["dig1 8 1 5 1", "dig2 3 6"]
# digit = [(let1, art can),(let2, own kit dig),(let3, art zero)]
#          (X[0], X[1]) 排序按照x[1]首字母排序后，如果相同字母，再按照x[0]排序
# 排序结束再复原每个词条- res += [x[0] + ' ' + x[1]]，加入结果返回

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter = []
        digit = []
        res = []

        # 依据id后面第1个元素，分成数字和字母两类，其中字母类以（id, content)存储
       
        for log in logs:
            lst = log.split(' ')
            if lst[1].isdigit():
                digit.append(log)
            elif lst[1].isalpha():
                letter.append((lst[0], ' '.join(lst[1:])))
         
         # 将字母类按照content 排序，再按照id排序
        letter.sort(key = lambda x:(x[1],x[0]))
        # 将他们分别复原，然后加入res
        for i in range(len(letter)):
            res += [letter[i][0] + " " +letter[i][1]]
        for i in range(len(digit)):
            res += [digit[i]]
        return res
        
        
