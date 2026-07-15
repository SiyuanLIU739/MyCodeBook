# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(root is None and subRoot is None):
            return True
        
        if(root is None and subRoot is not None):
            return False
        
        if(root is not None and subRoot is None):
            return True
        
        if(root.val == subRoot.val):
            return self.isIdentical(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isIdentical(self, rt1, rt2):
        if(rt1 is None and rt2 is None):
            return True
        if((rt1 is None) != (rt2 is None)):
            return False

        if(rt1.val != rt2.val):
            return False

        return self.isIdentical(rt1.left, rt2.left) and self.isIdentical(rt1.right, rt2.right) 