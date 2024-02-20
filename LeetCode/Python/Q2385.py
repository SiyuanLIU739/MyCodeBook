# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Node:
    def __init__(self, number):
        self.number = number
        self.tos = []
        self.layer = 10010
        self.visited = False

    def to(self, to):
        self.tos.append(to)



class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if(root == None):
            return 0

        self.n = 0

        queue = []

        rt = Node(root.val)

        self.buildGraph(root, rt, rt, queue, start)

        return self.bfs(queue)

    def buildGraph(self, rt, fatherNode, currentNode, queue, start):
        currentNode.to(fatherNode)
        self.n += 1

        if(currentNode.number == start):
            queue.append(currentNode)
            currentNode.visited = True
            currentNode.layer = 0

        if(rt.left != None):
            node = Node(rt.left.val)
            currentNode.to(node)
            self.buildGraph(rt.left, currentNode, node, queue, start)

        if(rt.right != None):
            node = Node(rt.right.val)
            currentNode.to(node)
            self.buildGraph(rt.right, currentNode, node, queue, start)

    def bfs(self, queue):
        ans = 0

        while(len(queue) != 0):
            fr = queue.pop()

            for to in fr.tos:
                if(to.visited == False):
                    to.visited = True

                    to.layer = fr.layer + 1
                    ans = max(ans, to.layer)

                    queue.insert(0, to)

        return ans

