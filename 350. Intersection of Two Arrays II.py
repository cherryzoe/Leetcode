# Given two arrays, write a function to compute their intersection.

# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

two pointers:
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = sorted(nums1)
        n2 = sorted(nums2)
        res = []
        
        i,j = 0, 0
        while i < len(n1) and j < len(n2):
            if n1[i] == n2[j]:
                res.append(n1[i])
                i += 1
                j += 1
            elif n1[i] > n2[j]:
                j += 1
            else:
                i += 1
        return res
        
        
use dictionary to count:

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        counter = collections.defaultdict(int)
        
        for i in nums1:
            counter[i] += 1
        
        
        for n in nums2:
            if counter[n] > 0:
                res.append(n)
                counter[n] -= 1
        return res
    
    
use Counter to make it cleaner:

class Solution(object):
    def intersect(self, nums1, nums2):

        counts = collections.Counter(nums1)
        res = []

        for num in nums2:
            if counts[num] > 0:
                res += num,
                counts[num] -= 1

        return res
    
def intersect(self, nums1, nums2):
    a, b = map(collections.Counter, (nums1, nums2))
    return list((a & b).elements())
    # elements(): 
    # Return an iterator over elements repeating each as many times as its count.
