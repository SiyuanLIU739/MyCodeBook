# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0

        self.dfs(root, root.val)

        return self.ans

    def dfs(self, rt, current_max):
        if(rt.val >= current_max):
            self.ans += 1

        if(rt.left is not None):
            self.dfs(rt.left, max(current_max, rt.val))

        if(rt.right is not None):
            self.dfs(rt.right, max(current_max, rt.val))