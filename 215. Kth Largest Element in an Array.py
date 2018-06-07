# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.

# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length

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
        
