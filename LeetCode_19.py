# 19. Remove Nth Node From End of List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        h1,h2 = head,head
        for i in range(n-1):
            if h1.next:
                h1 = h1.next
            else:
                return head
        h3 = None
        while h1.next != None:
            h1 = h1.next
            h3 = h2
            h2 = h2.next
        if not h3:
            return h2.next
        else:
            h3.next = h2.next
        return head