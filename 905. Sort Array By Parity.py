Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l,r = 0, len(A)-1
        while l <= r:
            while l <= r and A[l] %2 == 0:
                l += 1
            while l <= r and A[r] %2 != 0:
                r -= 1
            if l <= r:
                A[l], A[r] = A[r], A[l]
                l += 1
                r -= 1
        return A
