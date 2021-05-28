# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length

2021 Update:
   class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quickSort(nums, 0, len(nums)-1, k)

    def quickSort(self, nums, left, right, k):
        if left >= right:
            return nums[left]
        
        i, j  = left, right
        pivot = nums[random.randint(left, right)]
        while i <= j:
   
            while i <= j and  nums[i] > pivot:
                i += 1
            while i <= j and  nums[j] < pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        if  k-1 <= j:
            return self.quickSort(nums, left, j, k)
        else:
            return self.quickSort(nums, j+1, right, k)

Heap solution:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)

            # if len(heap) < k:
            #     heapq.heappush(heap, n)
            # else:
            #     top = heap[0]
            #     if n > top:
            #         heapq.heappop(heap)
            #         heapq.heappush(heap, n)
        return heap[0]

2020 Update:
解题思路： 用快速排序，大的放左边，小的放右边，如果左边大的个数大于K，则说明第K大的数必定在左边，因此只需要对左边进行递归，右边可不用再看了
   class Solution(object):
    def quickSort(self, nums, l, r, k):
        if l >= r:
            return nums[k]
        
        pivot = nums[l]
        i,j = l-1, r+1
        while i < j:
            i += 1
            while nums[i] > pivot:
                i += 1
            j -= 1
            while nums[j] < pivot:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        if k <= j:
            return self.quickSort(nums, l, j, k)
        else:
            return self.quickSort(nums, j+1, r, k)
    
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quickSort(nums, 0, len(nums)-1, k-1)
        

#Idea: use quicksort
   def findKthLargest(self, nums, k):
            def partition(nums, left, right):
                l,r = left+1, right
                pivot = nums[left]
                while l <= r:
                    if nums[l] < pivot and nums[r] > pivot:
                        nums[l], nums[r] = nums[r], nums[l]
                        l += 1
                        r -= 1
                    if nums[l] >= pivot:
                        l += 1
                    if nums[r] <= pivot:
                        r -= 1
                nums[left], nums[r] = nums[r], nums[left]
                return r

            left, right = 0, len(nums) - 1
            while True:    
                pos = partition(nums, left, right)
                if pos + 1 == k:
                    return nums[pos]
                elif pos + 1 > k:
                    right = pos - 1
                else:
                    left = pos + 1
        
