import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        skyline = []
        
        pq = [] 
        heapq.heapify(pq)

        i= 0
        n = len(buildings)

        while i < n or len(pq) > 0:
            if len(pq) == 0 or (i < n and buildings[i][0] <= pq[0][1]):
                cur_x = buildings[i][0]
                while i < n and cur_x == buildings[i][0]:
                    heapq.heappush(pq, (-buildings[i][2], buildings[i][1]))
                    i += 1
            else:
                cur_x = pq[0][1]
                while len(pq) > 0 and cur_x >= pq[0][1]:
                    heapq.heappop(pq)
            
            cur_h = -pq[0][0] if len(pq) > 0 else 0
            if len(skyline) == 0 or cur_h != skyline[-1][1]:
                skyline.append([cur_x, cur_h])
        
        return skyline