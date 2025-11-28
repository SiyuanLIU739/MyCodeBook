class Node:
    def __init__(self, i, value):
        self.number = i
        self.value = value
        self.sum = value
        self.to = []
        self.visited = False

    def add_to(self, to):
        self.to.append(to)

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # build nodes
        nodes = {}
        for i in range(n):
            nodes[i] = Node(i, values[i])

        # build edges
        for edge in edges:
            a = edge[0]
            b = edge[1]

            nodes[a].add_to(nodes[b])
            nodes[b].add_to(nodes[a])

        self.calculate_value(nodes[0])
        for i in range(n):
            print(nodes[i].sum)
        self.ans = 1

        for i in range(n):
            nodes[i].visited = False

        self.check_edges(nodes[0], k)

        return self.ans

    def calculate_value(self, node):
        node.visited = True

        for to in node.to:
            if(to.visited):
                continue

            self.calculate_value(to)
            node.sum += to.sum

    def check_edges(self, node, k):
        node.visited = True
        print(node.number, node.sum)
        for to in node.to:
            if(to.visited):
                continue
            if(to.sum % k == 0):
                self.ans += 1
            self.check_edges(to, k)