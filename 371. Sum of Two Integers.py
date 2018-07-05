# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

# Example:
# Given a = 1 and b = 2, return 3.

# Python 表示一个数不止32位. https://www.hrwhisper.me/leetcode-sum-two-integers/
# http://bookshadow.com/weblog/2016/06/30/leetcode-sum-of-two-integers/
# 因此。。做这题要保证两个数在正确的范围内（本题是int，32bit）

# 如何做到呢？我们知道32bit 可以表示的无符号整数位0~0xFFFFFFFF（全0~全1）

# 因此，我们使用&来保证该数是32bit.

# int的0和正整数范围为0~0x7FFFFFFF，int负数的范围为-0x80000000~-1,因此，大于0x7FFFFFFF的其实是最高位为1（这是符号位）。这样算出来是把最高位不当成符号位，我们还需要对负数的情况进行修正。

# 在具体实现上，我们可以先 &0x7FFFFFFF 然后取反，这样，-1变为-0x80000000(-2147483648) -2变为了-0x7FFFFFFF(-2147483647) ,因此，在^0x7FFFFFFF即可。。
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF
        MASK = 0x100000000
        
        if a == 0:
            return b
        if b == 0:
            return a
        
        while b != 0:
            _sum = (a ^ b)  % MASK  #calculate sum of a and b without thinking the carry 
            b = ((a & b)<<1) % MASK  #calculate the carry
            a = _sum  # add sum(without carry) and carry
        return a if a <= MAX_INT else ~((a & MAX_INT) ^ MAX_INT) #把31位之后的全部置1