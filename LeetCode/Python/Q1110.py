# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if(root is None):
            return []
        
        roots = set()
        self.dfs(root, roots, set(to_delete))
        
        return list(roots)
    
    def dfs(self, rt, roots, to_delete):
        if(rt.left is not None):
            self.dfs(rt.left, roots, to_delete)
        if(rt.right is not None):
            self.dfs(rt.right, roots, to_delete)

        if(rt.val not in to_delete):
            if(rt.left not in roots):
                rt.left = None
            else:
                roots.remove(rt.left)
            if(rt.right not in roots):
                rt.right = None
            else:
                roots.remove(rt.right)

            roots.add(rt)