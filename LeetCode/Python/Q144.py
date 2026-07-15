# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        if(root is None):
            return self.ans

        self.dfs(root)

        return self.ans
        
    def dfs(self, rt):
        self.ans.append(rt.val)

        if(rt.left is not None):
            self.dfs(rt.left)
        if(rt.right is not None):
            self.dfs(rt.right)