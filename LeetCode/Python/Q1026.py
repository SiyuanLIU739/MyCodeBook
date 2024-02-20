# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        self.bfs(root, root.val, root.val)

        return self.ans
    
    def bfs(self, rt, maxans, minans):
        if(rt == None):
            return
        
        self.ans = max(max(self.ans, abs(rt.val - maxans)), abs(rt.val - minans))

        if(rt.left != None):
            self.bfs(rt.left, max(maxans, rt.val), min(minans, rt.val))
        if(rt.right != None):
            self.bfs(rt.right, max(maxans, rt.val), min(minans, rt.val))