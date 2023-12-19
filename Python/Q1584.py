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

        self.number = n

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
    


class Solution:
    def minCostConnectPoints(self, points) -> int:
        ans = 0

        union = Union(len(points))
        edges = self.buildEdges(points)
        edges.sort(key = lambda x: x.length)

        for edge in edges:
            a = edge.a
            b = edge.b
            if(union.isInSameGroup(a, b)):
                continue

            union.merge(a, b)
            ans += edge.length

        return ans

    def buildEdges(self, points):
        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i, n):
                edges.append(Edge(i, j, self.length(points[i], points[j])))
        
        return edges

    def length(self, a, b):
        return self.abs(a[0] - b[0]) + self.abs(a[1] - b[1])
    
    def abs(self, x):
        if(x >= 0):
            return x
        return -x
    
if __name__ == "__main__":
    solver = Solution()
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    print(solver.minCostConnectPoints(points))