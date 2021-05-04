# 面试题 02.01. 移除重复节点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev, cur = head, head.next
        l = [prev.val]
        while cur and cur.next:
            if cur.val not in l:
                l.append(cur.val)
                prev = prev.next
                cur = cur.next
            else:
                while cur and cur.val in l:
                    cur = cur.next
                if not cur:
                    prev.next = None
                else:
                    prev.next = cur
                    l.append(cur.val)
                    prev = prev.next
                    cur = cur.next
        if cur and cur.val in l:
            prev.next = None
        return head

'''
        if not head:
            return head
        r = head
        record = {head.val}
        while r and r.next:
            if r.next.val not in record:
                record.add(r.next.val)
                r = r.next
            else:
                r.next = r.next.next
            
        return head
'''