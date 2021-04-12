# There is a fence with n posts, each post can be painted with one of the k colors.

# You have to paint all the posts such that no more than two adjacent fence posts have the same color.

# Return the total number of ways you can paint the fence.

# Note:
# n and k are non-negative integers.
定义 f[n] 表示 n 个栅栏时的总方案数。

1、当 n 为 1 时，上色方案数为 f[1] = k；

2、当 n 为 2 时，第 2 个栅栏的颜色可以和第 1 个一样，也可以不一样，因此总共有 f[2] = f[1] ×
k = k × k 个方案数；

3、当 n > 3 时，给第 n 个栅栏上色时，有两种选择：
3.1 和上一个不同颜色，那么此时第 n 个可以选的颜色有 k-1 个，截至到 n-1 的方案数为 f[n-1]，于是此时的方案总数为：f[n-1] × (k-1)
3.2 和上一个相同颜色，那么上一个就不能和上上一个同色，第 n 个可以选的颜色有 k-1 个，第 n-1 个可以选的颜色只有一个，那就是和第 n 个一样的那个，
因此截至 n-1 的方案数为 f[n-2] × 1，于是此时的方案总数为：f[n-2] × 1 × (k-1)；
3.3 合计两个情况，给 n 个栅栏上色总共有 f[n] = f[n - 1] × (k - 1) + f[n - 2] × (k - 1)

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [0] * (n+1)
        if n == 1:
            return k
        if n == 2:
            return k*k
        dp[1] = k
        dp[2] = k * k
        for i in range(3, n+1):
            # if i is same with i-1, we see them as bundle, select from k-1 solutions based on dp[n-2]
            # if i is different with previous i-1, then it will have k-1 solutions based on dp[n-1]
            dp[i] = dp[i-1] * (k-1) + dp[i-2] * (k-1)
        # print dp
        return dp[-1]
    
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
#         when there is no fence, we have no option to paint then return 0
        if n == 0:
            return 0
#         when there is only one fence, we have option for all color to paint it
        if n == 1:
            return k
#         as it comes to 2 fence, the 2nd fence has 2 option:
#             - same with 1st fence then all option should be k * 1
#             - diff with 1st then all option should be k * (k-1)
        same = k
        diff = k * (k-1)
#         as it comes to 3 or more fence, each one fence option are based on previous fence painting color decision
#             if 3rd if same with previous one(2nd) then 2nd must be difference with 1st: k * (k-1) * 1 => previous diff
#             if diff with previous one then 2nd can same/diff with previous one: diff = same + diff
        for i in range(3, n+1):
            prevDiff = diff
            diff = (same + diff) * (k-1)
            same = prevDiff 
        return same + diff
        
Solution 2: O(n) space
class Solution(object):
    def numWays(self, n, k):
       
        if n == 0:
            return 0
        if n == 1:
            return k
        dp = [0] * n
#         when it comes to the 1st fence, it can choose k colors
        dp[0] = k
#     when it comes to 1st and 2nd fence, total option can be
#         - 1st is same with 2nd: k * 1
#         - 1st is diff with 2nd: k * (k-1)
#       total = k + k*(k-1) = k*k
        dp[1] = k*k
        for i in range(2, n):
            dp[i] = (k-1) * (dp[i -1] + dp[i -2])
        return dp[n-1]

Solution3 preferred:
    if n == 1:
        return k
    if n == 2:
        return K*K
    dif, same = k*(k-1), k
    for i in range(3, n+1):
        same, dif = dif, (dif + same) * (k-1)
    return dif+same
