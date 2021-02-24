# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # brute force, create list of all elements in all lists, sort and create new linked list
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l_all_ele = []
        for l in lists:
            while l:
                l_all_ele.append(l.val)
                l = l.next
        res = ListNode(0)
        head = res
        for ele in sorted(l_all_ele):
            res.next = ListNode(ele)
            res = res.next
        return head.next
    # Merge lists one by one
    '''
        while len(lists) > 1:
            temp = merge_two_list(lists[0], lists[1])
            lists.pop(0)
            lists[0] = temp
    '''