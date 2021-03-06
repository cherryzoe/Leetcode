# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.


# Example

# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

tips:
1. sorted(people, key = lambda(h,k):(-h,k)) => sort by height decrease, if height is same, sort by k(by default incrase)
2. after sorted, we get [7,0] [7,1] [6,1] [5,2] [4,4] we know that [4,4]no mater which position to be inserted, it will not affect rest as it's the smallest. so we insert the smaller later among larger numbers. we put the large numbers first in the position first. 

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        res = []
#         To use key= custom sorting, 
#         remember that you provide a function that takes one value 
#         and returns the proxy value to guide the sorting.
        people = sorted(people, key = lambda(h,k):(-h,k))
        for p in people:
            res.insert(p[1], p) #insert(position, value)
        return res
