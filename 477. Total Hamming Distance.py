# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Now your job is to find the total Hamming distance between all pairs of the given numbers.

# Example:
# Input: 4, 14, 2

# Output: 6

# Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
# showing the four bits relevant in this case). So the answer will be:
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
# Note:
# Elements of the given array are in the range of 0 to 10^9
# Length of the array will not exceed 10^4.

# 思路： 
# 我们需要来找出某种规律来，比如我们看下面这个例子，4，14，2和1：

# 4:     0 1 0 0
# 14:    1 1 1 0
# 2:     0 0 1 0
# 1:     0 0 0 1

# 我们先看最后一列，有三个0和一个1，那么它们之间相互的汉明距离就是3，即1和其他三个0分别的距离累加，
# 然后在看第三列，累加汉明距离为4，因为每个1都会跟两个0产生两个汉明距离，同理第二列也是4，第一列是3。
# 我们仔细观察累计汉明距离和0跟1的个数，我们可以发现其实就是0的个数乘以1的个数，发现了这个重要的规律，那么整道题就迎刃而解了，
# 只要统计出每一位的1的个数即可

# slution1:
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        list = zip(*map('{:032b}'.format,(nums)))
        for i in list:         
            sum += i.count('0') * i.count('1')
        return sum
        
# solution 2 - similar solution with bit manipulate:
    class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask = 1
        res = 0
        
        for i in range(0, 32):
            ones =  zeros = 0
            for n in nums:
                if n & mask:
                    ones += 1
                else:
                    zeros += 1
            res += ones * zeros
            mask = mask << 1
        return res
    
    
# solution3 - Brute Force ( over time limit)
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                res += self.helper(nums[i], nums[j])
                j += 1
            i += 1
        return res
        
    def helper(self, x, y):
        cnt = 0
        xor = x ^ y
        while xor:
            cnt += 1
            xor = xor & (xor-1)
        return cnt
