# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.diff = 1000000
        self.last = -1000000

        self.dfs(root)

        return self.diff
    
    def dfs(self, rt):
        if(rt is None):
            return
        
        self.dfs(rt.left)
        self.diff = min(self.diff, rt.val - self.last)
        self.last = rt.val
        self.dfs(rt.right)