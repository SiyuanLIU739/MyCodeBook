# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        while(root is not None):
            if(root.val > high):
                root = root.left
            elif(root.val < low):
                root = root.right
            else:
                break

        self.trimLeft(root, low)
        self.trimRight(root, high)
        
        return root
    
    def trimLeft(self, rt, low):
        if(rt is None):
            return
        
        if(rt.left is not None):
            if(rt.left.val < low):
                rt.left = rt.left.right
                self.trimLeft(rt, low)
            else:
                self.trimLeft(rt.left, low)

    def trimRight(self, rt, high):
        if(rt is None):
            return
        
        if(rt.right is not None):
            if(rt.right.val > high):
                rt.right = rt.right.left
                self.trimRight(rt, high)
            else:
                self.trimRight(rt.right, high)