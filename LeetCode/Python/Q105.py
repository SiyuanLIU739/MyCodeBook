# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if(len(preorder) == 0):
            return None
        
        node = TreeNode(preorder[0], None, None)
        if(len(preorder) == 1):
            return node
        
        mid = -1
        for i in range(len(inorder)):
            if(inorder[i] == preorder[0]):
                mid = i
                break

        left = self.buildTree(preorder[1: mid + 1], inorder[: mid])
        right = self.buildTree(preorder[mid + 1: ], inorder[mid + 1: ])

        node.left = left
        node.right = right
        
        return node