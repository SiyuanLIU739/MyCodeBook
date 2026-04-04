# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ret = []
        if(root.left is not None):
            ret.extend(self.binaryTreePaths(root.left))
        if(root.right is not None):
            ret.extend(self.binaryTreePaths(root.right))
            
        if(len(ret) == 0):
            ret.append(str(root.val))
        else:
            for i in range(len(ret)):
                r = ret[i]
                r = str(root.val) + '->' + r
                ret[i] = r

        return ret