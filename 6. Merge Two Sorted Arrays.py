Merge two given sorted integer array A and B into a new sorted integer array.
Example
A=[1,2,3,4]

B=[2,4,5,6]

return [1,2,2,3,4,4,5,6]

Solution:
class Solution:
    """
    @param: A: sorted integer array A
    @param: B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        m,n = 0, 0
        res = []
        while m < len(A) and n < len(B):
            if A[m] < B[n]:
                res.append(A[m])
                m += 1
            else:
                res.append(B[n])
                n += 1
        if m < len(A):
            res = res+A[m:]
        if n < len(B):
            res = res+B[n:]
        return res
