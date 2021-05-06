# 面试题 02.06. 回文链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return l == l[::-1]