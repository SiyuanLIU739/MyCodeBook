from queue import PriorityQueue

class Edge:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def __lt__(self, other) -> bool:
        if(self.a == other.a):
            return self.b < other.b
        return self.a < other.a



class Solution:
    def minCostConnectPoints(self, points) -> int:
        added = [0]
        ans = 0

        edges = PriorityQueue(len(points) * (len(points) - 1) / 2)

        for i in range(1, len(points)):
            length = self.calLength(points[0], points[i])
            edges.put((length, Edge(0, i)))

        while(len(added) != len(points)):
            a = edges.get()
            edge = a[1]
            length = a[0]
            
            t = edge.b
            if(t in added):
                continue

            added.append(t)
            ans += length

            for i in range(len(points)):
                if(i in added):
                    continue
                
                length = self.calLength(points[t], points[i])
                edges.put((length, Edge(t, i)))

        return ans

    def calLength(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    

if __name__ == "__main__":
    sol = Solution()
    points = [[0,0],[0,1],[1,1]]
    print(sol.minCostConnectPoints(points))

