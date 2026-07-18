class Node:
    def __init__(self, val = 0):
        self.val = val
        self.ancestor = val

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        nodes = [None]
        for i in range(n):
            nodes.append(Node(i + 1))
        
        for edge in edges:
            x, y = edge[0], edge[1]

            anc_x = self.findAncestor(nodes[x], nodes)
            anc_y = self.findAncestor(nodes[y], nodes)

            if(anc_x == anc_y):
                return edge
            
            nodes[nodes[x].ancestor].ancestor = y

        return None
    
    def findAncestor(self, node, nodes):
        if(node.val != node.ancestor):
            anc = self.findAncestor(nodes[node.ancestor], nodes)
            node.ancestor = anc
            return anc
        
        return node.val