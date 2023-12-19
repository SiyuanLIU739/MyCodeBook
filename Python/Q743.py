class Edge:
    def __init__(self, to, w):
        self.to = to
        self.w = w

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        inf = 6000 * 100 * 10

        edges = [None]

        for i in range(n):
            edges.append([])

        for time in times:
            edges[time[0]].append(Edge(time[1], time[2]))

        dis = [0]
        for i in range(n):
            dis.append(inf)

        dis[k] = 0
        for edge in edges[k]:
            dis[edge.to] = edge.w
        s = [k]
        while(True):
            v = 0
            disv = inf
            for i in range(1, n + 1):

                if(i in s):
                    continue

                if(dis[i] < disv):
                    v = i
                    disv = dis[i]

            if(v == 0):
                break
            s.append(v)

            for edge in edges[v]:
                dis[edge.to] = self.min(dis[edge.to], dis[v] + edge.w)

        ans = 0
        for i in range(1, n + 1):
            if(ans < dis[i]):
                ans = dis[i]


        if(ans == inf):
            return -1
        
        return ans

    def min(self, a, b):
        if(a > b):
            return b
        return a