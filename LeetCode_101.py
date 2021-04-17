# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.dfs(root.left, root.right)
    
    def dfs(self, left, right):
        if not left and not right:
            return True
        if not (left and right):
            return False
        if left.val != right.val:
            return False
        return self.dfs(left.left, right.right) and self.dfs(left.right, right.left)
