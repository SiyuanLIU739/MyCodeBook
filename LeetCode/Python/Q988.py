# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans = 'z' * 8500

        self.dfs(root, "")
        
        return self.ans
    
    def dfs(self, rt, str):
        current = chr(rt.val + ord('a')) + str

        if(self.isLeaf(rt)):
            if(self.ans > current):
                self.ans = current
            
            return
        
        if(rt.left is not None):
            self.dfs(rt.left, current)

        if(rt.right is not None):
            self.dfs(rt.right, current)

    def isLeaf(self, rt):
        return ((rt.left is None) and (rt.right is None))