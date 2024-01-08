# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        self.search(root, low, high)
        return self.ans
    
    def search(self, rt, low, high):
        if(rt == None):
            return
        
        if((low >= rt.val) and (high <= rt.val)):
            self.ans += rt.val

        if(rt.left != None):
            self.search(rt.left, low, high)
        if(rt.right != None):
            self.search(rt.right, low, high)