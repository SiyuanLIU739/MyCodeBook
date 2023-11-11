class Graph:
    def min(self, a, b):
        if(a > b):
            return b
        return a
    
    def __init__(self, n: int, edges):
        self.dist = []
        inf = 100000005

        for i in range(n):
            lst = []
            for j in range(n):
                lst.append(inf)
            self.dist.append(lst)
        
        for edge in edges:
            fr = edge[0]
            to = edge[1]
            p = edge[2]

            self.dist[fr][to] = self.min(self.dist[fr][to], p)

        for i in range(n):
            self.dist[i][i] = 0

        for i in range(n):
            for fr in range(n):
                for to in range(n):
                    self.dist[fr][to] = self.min(self.dist[fr][to], self.dist[fr][i] + self.dist[i][to])
        

    def addEdge(self, edge) -> None:
        fr = edge[0]
        to = edge[1]
        p = edge[2]

        if(self.dist[fr][to] > p):
            self.dist[fr][to] = p

            n = len(self.dist)
            for i in range(n):
                for j in range(n):
                    self.dist[i][j] = min(self.dist[i][j], self.dist[i][fr] + self.dist[to][j] + p)
            

    def shortestPath(self, node1: int, node2: int) -> int:
        inf = 100000005

        return self.dist[node1][node2] if self.dist[node1][node2] != inf else -1
