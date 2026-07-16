# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.findNode(root, p)
        q_path = self.findNode(root, q)

        if(len(p_path) > len(q_path)):
            t = p_path
            p_path = q_path
            q_path = t

        for i in range(1, len(p_path) + 1):
            if(p_path[-i].val != q_path[-i].val):
                return p_path[-i + 1]
            
        return p_path[0]
    
    def findNode(self, rt, p):
        if(p.val == rt.val):
            return [p]
        
        if(rt.left is not None):
            path = self.findNode(rt.left, p)
            if(len(path) != 0):
                path.append(rt)
                return path
            
        if(rt.right is not None):
            path = self.findNode(rt.right, p)
            if(len(path) != 0):
                path.append(rt)
                return path
            
        return []