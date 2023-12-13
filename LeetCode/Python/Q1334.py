
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dis = []
        inf = 100 * 10000

        for i in range(n):
            lst = []
            for j in range(n):
                lst.append(inf)
            dis.append(lst)
            dis[i][i] = 0

        for edge in edges:
            fr = edge[0]
            to = edge[1]
            w = edge[2]

            dis[fr][to] = w
            dis[to][fr] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

        ans = -1
        number = n
        for i in range(n):
            count = 0
            for j in range(n):
                if(j == i):
                    continue
                if(dis[i][j] <= distanceThreshold):
                    count += 1

            if(count <= number):
                ans = i
                number = count

        return ans