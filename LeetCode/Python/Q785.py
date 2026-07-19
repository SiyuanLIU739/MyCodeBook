from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        colors = [None] * n

        q = deque()
        for i in range(n):
            if(colors[i] is None):
                colors[i] = False
                q.append(i)
                
                while(q):
                    fr = q.popleft()
                    for to in graph[fr]:
                        if(colors[to] is None):
                            colors[to] = not colors[fr]
                            q.append(to)
                        else:
                            if(colors[to] == colors[fr]):
                                return False
                            
        return True