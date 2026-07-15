# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.inorder = []
        self.dfsInorder(root)

        backSum = [0]
        for num in reversed(self.inorder):
            backSum.append(backSum[-1] + num)
        self.backSum = list(reversed(backSum))
        self.backSum.pop()

        self.dfsConvert(root)

        return root

    def dfsInorder(self, root):
        if(root is None):
            return
        
        self.dfsInorder(root.left)
        self.inorder.append(root.val)
        self.dfsInorder(root.right)

    def dfsConvert(self, root):
        if(root is None):
            return
        
        self.dfsConvert(root.right)
        root.val = self.backSum.pop()
        self.dfsConvert(root.left)