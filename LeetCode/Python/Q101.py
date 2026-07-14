# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if(root.left is None and root.right is None):
            return True
        
        if(root.left is None or root.right is None):
            return False
        
        return self.dfs(root.left, root.right)
    
    def dfs(self, left, right):
        if(left.val != right.val):
            return False
        
        if((left.left is None) != (right.right is None)):
            return False
        
        if((left.right is None) != (right.left is None)):
            return False
        

        sym = True
        if(left.left is not None):
            sym = self.dfs(left.left, right.right)
        if(not sym):
            return False
        
        if(left.right is not None):
            sym = self.dfs(left.right, right.left)
        if(not sym):
            return False
        
        return True