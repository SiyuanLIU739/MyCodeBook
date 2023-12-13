# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root) -> float:
        self.ans = 0

        sum, n = self.avgSubTree(root)

        if(sum / n > self.ans):
            self.ans = sum / n

        return self.ans
    
    def avgSubTree(self, rt):
        if(rt == None):
            return (0, 0)
        
        sum1, n1 = self.avgSubTree(rt.left)
        sum2, n2 = self.avgSubTree(rt.right)

        sum = sum1 + sum2 + rt.val
        n = n1 + n2 + 1

        if(sum / n > self.ans):
            self.ans = sum / n

        return (sum, n)
