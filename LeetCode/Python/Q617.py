# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if(root1 is None and root2 is None):
            return None
        
        root = TreeNode()
        if(root1 is not None):
            root.val += root1.val
        if(root2 is not None):
            root.val += root2.val

        root.left = self.mergeTrees(root1.left if root1 is not None else None, root2.left if root2 is not None else None)
        root.right = self.mergeTrees(root1.right if root1 is not None else None, root2.right if root2 is not None else None)

        return root