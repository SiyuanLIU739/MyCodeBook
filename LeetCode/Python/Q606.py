# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root) -> str:
        self.str = ""

        self.tostr(root)

        return self.str
    
    def tostr(self, rt):
        self.str += str(rt.val)

        if(rt.left == None and rt.right == None):
          return

        self.str += '('
        if(rt.left != None):
            self.tostr(rt.left)
        self.str += ')'

        
        if(rt.right != None):
            self.str += '('
            self.tostr(rt.right)
            self.str += ')'