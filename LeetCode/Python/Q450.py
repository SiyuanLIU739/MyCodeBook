# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if(root is None):
            return None
        
        if(root.val == key):
            if(root.left is None):
                return root.right
            
            if(root.right is None):
                return root.left
            
            a = root.left
            b = root.right
            c = a.right
            d = b
            while(d.left is not None):
                d = d.left
            a.right = b
            d.left = c
            return a

        if(root.val > key):
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root