# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root is None):
            return 0

        return self.dfs(root, 1)
    
    def dfs(self, rt, depth):
        dp = depth

        if(rt.left is not None):
            dp = max(dp, self.dfs(rt.left, depth + 1))
        
        if(rt.right is not None):
            dp = max(dp, self.dfs(rt.right, depth + 1))
        
        return dp