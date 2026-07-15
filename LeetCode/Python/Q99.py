# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inorder = []
        self.dfs(root)

        last = None
        for i in range(1, len(self.inorder)):
            if(self.inorder[i].val < self.inorder[i - 1].val):
                last = self.inorder[i]
        
        first = None
        for i in range(len(self.inorder)):
            if(self.inorder[i].val > last.val):
                first = self.inorder[i]
                break

        fv = first.val
        first.val = last.val
        last.val = fv

    def dfs(self, rt):
        if(rt.left is not None):
            self.dfs(rt.left)
        
        self.inorder.append(rt)

        if(rt.right is not None):
            self.dfs(rt.right)
