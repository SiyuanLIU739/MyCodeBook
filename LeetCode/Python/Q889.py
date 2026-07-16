# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if(len(preorder) == 0):
            return None
        
        root = TreeNode(val = preorder[0])

        if(len(preorder) == 1):
            return root
        
        lastLeft = 0
        while(postorder[lastLeft] != preorder[1]):
            lastLeft += 1

        root.left = self.constructFromPrePost(preorder[1: 2 + lastLeft], postorder[: 1 + lastLeft])
        root.right = self.constructFromPrePost(preorder[2 + lastLeft: ], postorder[lastLeft + 1: ])

        return root
