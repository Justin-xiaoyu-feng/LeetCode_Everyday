# 2. Add Two Numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry_over = 0 
        curr_one = l1
        curr_two = l2
        result = None
        rslt_end = result
        
        
        while(curr_one or curr_two):
            sum_two_nodes = carry_over
            carry_over = 0
            
            if curr_one:
                sum_two_nodes += curr_one.val    
                curr_one = curr_one.next
            if curr_two:
                sum_two_nodes += curr_two.val
                curr_two = curr_two.next
                
            if sum_two_nodes >= 10:
                carry_over += 1
                sum_two_nodes %= 10
            
            
            node = ListNode(val=sum_two_nodes)
            if result:
                rslt_end.next = node
                rslt_end = rslt_end.next
            else:
                result = node
                rslt_end = result
            
            sum_two_nodes = 0
            
            
        if carry_over > 0:
            rslt_end.next = ListNode(val=1)
        return result