class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = [[p, p[0] ** 2 + p[1] ** 2] for p in points]

        dis.sort(key = lambda x: x[1])

        ans = []
        for i in range(k):
            ans.append(dis[i][0])

        return ans