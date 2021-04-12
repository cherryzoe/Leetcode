

# The read4 API is already defined for you.
# @param buf4, List[str]
# @return an integer
# def read4(buf4):

class Solution(object):
    def __init__(self):
        self.buf = []

    def read(self, buf, n):
        """
        :type buf: List[str]
        :type n: int
        :rtype: int
        """
        buf_len = len(self.buf)

        if buf_len >= n:
            buf[:n] = self.buf[:n]
            self.buf = self.buf[n:]
            return n
        
        cur = buf_len
        while cur < n:
            cache = [''] * 4
            num = read4(cache)
            if num == 0:
                break
            cur += num
            self.buf += cache
        res = min(n, cur)
        buf[:res] = self.buf[:res]
        self.buf = self.buf[res:]
        return res
