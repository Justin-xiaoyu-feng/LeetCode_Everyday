# 21. Merge Two Sorted Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        h1, h2 = l1, l2
        # recursive solution, if h1.val < h2.val, h1.next should be merge(h1.next, h2)...
        # if one of h1,h2 empty, just add the other one after
        if h1.val < h2.val:
            h1.next = self.mergeTwoLists(h1.next, h2)
            return h1
        else:
            h2.next = self.mergeTwoLists(h1, h2.next)
            return h2