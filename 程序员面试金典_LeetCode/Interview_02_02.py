# 面试题 02.02. 返回倒数第 k 个节点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        l = head
        for i in range(k):
            l = l.next
        while l:
            l = l.next
            head = head.next
        return head.val