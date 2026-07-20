import heapq

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = [[None] * n for _ in range(n)]
        utilization = [[0] * n for _ in range(n)]

        for edge in edges:
            fr = edge[0]
            to = edge[1]
            subs = edge[2]

            graph[fr][to] = subs
            graph[to][fr] = subs

        visited = [False] * n

        q = [(0, 0)]
        while(q):
            move, fr = heapq.heappop(q)

            if(visited[fr]):
                continue
            visited[fr] = True
            
            for to in range(n):
                if(graph[fr][to] is None):
                    continue
                    
                if(move + graph[fr][to] + 1 <= maxMoves):
                    heapq.heappush(q, (move + graph[fr][to] + 1, to))
                    utilization[fr][to] = graph[fr][to]
                
                else:
                    utilization[fr][to] = maxMoves - move


        ans = 0
        for fr in range(n):
            if(visited[fr]):
                ans += 1
            for to in range(fr + 1, n):
                ans += min(graph[fr][to] if graph[fr][to] is not None else 0, utilization[fr][to] + utilization[to][fr])

        return ans
