# Count how many nodes in a linked list.

# Have you met this question in a real interview? Yes
# Example
# Given 1->3->5, return 3

 def countNodes(self, head):
        # write your code here
        cnt = 0
        while head:
            cnt += 1
            head = head.next
        return cnt
     
