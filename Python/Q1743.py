class Solution:
    def addEdge(self, a, b, edges):
        edge = []

        if(a in edges.keys()):
            edge = edges[a]
        
        edge.append(b)

        edges[a] = edge
    
    def restoreArray(self, adjacentPairs):
        edges = {}
        for pair in adjacentPairs:
            a = pair[0]
            b = pair[1]

            self.addEdge(a, b, edges)
            self.addEdge(b, a, edges)

        meet = []
        ans = []

        for i in edges.keys():
            if(i in meet):
                continue

            tos = edges[i]

            if(len(tos) != 1):
                continue

            ans.append(i)
            meet.append(i)

            to = tos[0]

            while(len(edges[to]) != 1):
                ans.append(to)
                meet.append(to)

                if(edges[to][0] in meet):
                    to = edges[to][1]
                else:
                    to = edges[to][0]

            ans.append(to)
            meet.append(to)

        return ans

