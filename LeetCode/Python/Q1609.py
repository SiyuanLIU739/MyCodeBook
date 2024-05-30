# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        self.level = {}
        
        return self.dfs(root, 0)
    
    def dfs(self, rt, lv):
        ret = self.check(lv, rt.val)
        if(ret == False):
            return False
        else:
            self.level[lv] = rt.val

        if(self.left is not None):
            ret = self.dfs(rt.left, lv + 1)
        if(ret == False):
            return False
        if(self.right is not None):
            ret = self.dfs(rt.right, lv + 1)
        if(ret == False):
            return False
        
        return True
        


    def check(self, lv, val):
        if(lv % 2 == 0):
            if(lv not in self.level.keys()):
                self.level[lv] = 0

            if(val <= self.level[lv]):
                return False
        else:
            if(lv not in self.level.keys()):
                self.level[lv] = 1000000
            
            if(val >= self.level[lv]):
                return False
            
        return True