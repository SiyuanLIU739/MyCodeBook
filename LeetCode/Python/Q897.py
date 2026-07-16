# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.fakeRoot = TreeNode()
        self.last = self.fakeRoot

        self.dfs(root)
        return self.fakeRoot.right
    
    def dfs(self, rt):
        if(rt is None):
            return
        
        self.dfs(rt.left)

        self.last.right = rt
        self.last = rt
        rt.left = None

        self.dfs(rt.right)