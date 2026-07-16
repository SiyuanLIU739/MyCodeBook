# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        self.ans = 0

        self.dfs(root, distance)

        return self.ans
    
    def dfs(self, rt, distance):
        if(rt is None):
            return {0: 0}
        
        if(rt.left is None and rt.right is None):
            return {0: 1}
        
        left = self.dfs(rt.left, distance)
        right = self.dfs(rt.right, distance)

        for kl, vl in left.items():
            for kr, vr in right.items():
                if(kl + kr + 2 <= distance):
                    self.ans += (vl * vr)

        this = {}
        for k, v in left.items():
            if(v != 0):
                if(k + 1 not in this.keys()):
                    this[k + 1] = 0
                this[k + 1] += v

        for k, v in right.items():
            if(v != 0):
                if(k + 1 not in this.keys()):
                    this[k + 1] = 0
                this[k + 1] += v

        return this


        
