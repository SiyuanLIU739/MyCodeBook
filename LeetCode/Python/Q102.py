# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        ans = []
        
        if(not root):
            return ans
            
        q.append((root, 0))
        while(q):
            node, layer = q.popleft()

            if(len(ans) == layer):
                ans.append([])
            ans[layer].append(node.val)

            if(node.left is not None):
                q.append((node.left, layer + 1))
            if(node.right is not None):
                q.append((node.right, layer + 1))

        return ans