class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if(len(inorder) == 0):
            return None
            
        val = postorder.pop()
        root = TreeNode(val = val)

        if(len(inorder) == 1):
            return root

        mid = 0
        while(inorder[mid] != val):
            mid += 1

        root.left = self.buildTree(inorder[: mid], postorder[: mid])
        root.right = self.buildTree(inorder[mid + 1: ], postorder[mid: ])

        return root