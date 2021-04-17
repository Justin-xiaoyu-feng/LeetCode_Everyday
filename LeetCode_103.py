# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        stack = [[root]]
        count = 0
        while stack:
            cur = stack.pop()
            temp = []
            buf = []
            for ele in cur:
                if ele.left:
                    temp.append(ele.left)
                if ele.right:
                    temp.append(ele.right)
                buf.append(ele.val)
            if count%2 == 1:
                res.append(buf[::-1])
            else:
                res.append(buf)
            count += 1
            if temp:
                stack.append(temp)
        return res