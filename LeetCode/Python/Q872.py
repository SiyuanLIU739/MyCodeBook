# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        rt1 = []
        rt2 = []

        self.search(root1, rt1)
        self.search(root2, rt2)

        return rt1 == rt2
    
    def search(self, rt, lst):
        if(rt.left != None):
            self.search(rt.left, lst)
        if(rt.right != None):
            self.search(rt.right, lst)
        if(rt.left == None and rt.right == None):
            lst.append(rt.val)