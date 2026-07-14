from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()

        sums = [0] * 10000
        nodes = [0] * 10000

        q.append((root, 0))

        while(q):
            rt, layer = q.popleft()
            sums[layer] += rt.val
            nodes[layer] += 1

            if(rt.left is not None):
                q.append((rt.left, layer + 1))
            if(rt.right is not None):
                q.append((rt.right, layer + 1))

        ans = []
        for i in range(10000):
            if(nodes[i] == 0):
                break

            ans.append(sums[i] / nodes[i])

        return ans