# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if(root is None):
            return True
        
        return self.dfs(root) != -1
    
    def dfs(self, rt):
        left = 0
        if(rt.left is not None):
            left = self.dfs(rt.left)
        if(left < 0):
            return -1
        
        right = 0
        if(rt.right is not None):
            right = self.dfs(rt.right)
        if(right < 0):
            return -1
        
        if(abs(left - right) <= 1):
            return max(left, right) + 1
        return -1