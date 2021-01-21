格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。

给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。

格雷编码序列必须以 0 开头。


示例 1:

输入: 2
输出: [0,1,3,2]
解释:
00 - 0
01 - 1
11 - 3
10 - 2

对于给定的 n，其格雷编码序列并不唯一。
例如，[0,2,3,1] 也是一个有效的格雷编码序列。

00 - 0
10 - 2
11 - 3
01 - 1

特判 当输入 0 的时候输出0，1的时候输出【0，1】
然后每次的是基于上一次的greycode 镜像对称成双倍，前一半末尾补0（相当于*2），后一般末尾补1（相当于*2后再+1）

比如1 = 【0， 1】
2 = 镜像1的greycode得到【0，1，1，0】，前半部分*2得到，后半部分加1【00，10，11，01】

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """


        res = [0, 1]
        
        if n == 0:
            return 0

        for i in range(n-1):
            for j in range(len(res)-1, -1, -1):
                res[j] *= 2
                res.append(res[j]+1)
        return res
