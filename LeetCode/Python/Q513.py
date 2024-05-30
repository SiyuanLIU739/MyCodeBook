# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.leftLeaf = [root.val]

        self.dfs(root, 0)

        return self.leftLeaf[-1]
    
    def dfs(self, rt, lv):
        if(rt.left is not None):
            if(len(self.leftLeaf) == lv + 1):
                self.leftLeaf.append(rt.left.val)

            self.dfs(rt.left, lv + 1)

        if(rt.right is not None):
            if(len(self.leftLeaf) == lv + 1):
                self.leftLeaf.append(rt.right.val)
                
            self.dfs(rt.right, lv + 1)