class Edge:
    def __init__(self, a, b, length) -> None:
        self.a = a
        self.b = b
        self.length = length



class Union:
    def __init__(self, n: int):
        self.father = []
        self.size = []
        for i in range(n):
            self.father.append(i)
            self.size.append(1)

        self.number = n - 1

    def merge(self, a: int, b: int):
        self.number -= 1

        fatherA = self.findFather(a)
        fatherB = self.findFather(b)
        if(self.size[fatherA] < self.size[fatherB]):
            self.father[fatherA] = fatherB
            self.size[fatherB] += self.size[fatherA]
        else:
            self.father[fatherB] = self.father[fatherA]
            self.size[fatherA] += self.size[fatherB]

    def findFather(self, node: int) -> int:
        if(self.father[node] == node):
            return node
        
        self.father[node] = self.findFather(self.father[node])
        return self.father[node]
    
    def isInSameGroup(self, a: int, b: int) -> bool:
        fatherA = self.findFather(a)
        fatherB = self.findFather(b)

        return (fatherA == fatherB)
    
    def getNumber(self):
        return self.number
    


class Solution:
    def minimumCost(self, n: int, connections) -> int:
        ans = 0

        union = Union(n + 1)
        edges = self.buildEdges(connections)
        edges.sort(key = lambda x: x.length)

        for edge in edges:
            a = edge.a
            b = edge.b
            if(union.isInSameGroup(a, b)):
                continue

            union.merge(a, b)
            ans += edge.length

        if(union.getNumber != 1):
            return -1

        return ans

    def buildEdges(self, pipes):
        edges = []

        n = len(pipes)
        for i in range(n):
            a = pipes[i][0]
            b = pipes[i][1]
            length = pipes[i][2]

            edges.append(Edge(a, b, length))
        
        return edges
