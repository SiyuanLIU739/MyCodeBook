# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if(root is None):
            return 0
            
        sums = {0: 1}
        self.ans = 0
        self.dfs(root, sums, targetSum, 0)

        return self.ans

    def dfs(self, rt, sums, target, current_sum):
        new_sum = current_sum + rt.val
        if(new_sum - target in sums.keys()):
            self.ans += sums[new_sum - target]
        
        if(new_sum not in sums.keys()):
            sums[new_sum] = 0
        sums[new_sum] += 1

        if(rt.left is not None):
            self.dfs(rt.left, sums, target, new_sum)
        if(rt.right is not None):
            self.dfs(rt.right, sums, target, new_sum)

        sums[new_sum] -= 1