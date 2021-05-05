# 面试题 02.05. 链表求和
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        s = ListNode(0)
        cur = s
        while l1 and l2:
            temp = l1.val + l2.val + carry
            if temp < 10:
                cur.next = ListNode(temp)
                carry = 0
            else:
                cur.next = ListNode(temp-10)
                carry = 1
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        if not l1:
            l1 = l2
        while l1:
            temp = l1.val + carry
            if temp < 10:
                cur.next = ListNode(temp)
                carry = 0
            else:
                cur.next = ListNode(0)
                carry = 1
            cur = cur.next
            l1 = l1.next
        if not carry:
            cur.next = None
        else:
            cur.next = ListNode(1)
            carry = 0
            cur.next.next = None
        return s.next