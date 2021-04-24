class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # 不断比较当前与下一个，当不一样时，把当前的存档，重置计数器移到下一个元素
        # 如果当前是最后元素，也停下来，一样的处理方式
        idx = -1
        i = 0
        cnt = 1
        while i < len(chars):
            while i < len(chars)-1 and chars[i] == chars[i+1]:
                cnt += 1
                i += 1
            # stops while i == len(chars) - 1 or chars[i] != chars[i+1]:
            # update results
            idx += 1
            chars[idx] = chars[i]
            if cnt > 1:
                strs = str(cnt)
                for s in strs:
                    idx += 1
                    chars[idx] = s
            # do not forget to reset cnt and i for the next while loop.
            cnt = 1        
            i += 1
        return idx + 1
        

        

