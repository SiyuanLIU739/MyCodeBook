# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
    
    def dfs(self, rt):
        if(rt is None):
            return
        
        # check left node = leaf?
        if(rt.left is not None and rt.left.left is None and rt.left.right is None):
            self.ans += rt.left.val
        
        self.dfs(rt.left)
        self.dfs(rt.right)
