There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

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
