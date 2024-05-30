# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        self.dfs(root, 0)

        return self.ans
    
    def dfs(self, rt, father):
        value = father * 10 + rt.val
        if(self.isLeaf(rt)):
            ans += (value)
            return
        
        if(rt.left is not None):
            self.dfs(rt.left, value)

        if(rt.right is not None):
            self.dfs(rt.right, value)

    def isLeaf(self, rt):
        return (rt.left is None) and (rt.right is None)
    
    