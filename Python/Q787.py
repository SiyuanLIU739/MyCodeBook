class Flight:
    def __init__(self) -> None:
        self.tos = []
        self.price = []

    def add_flight(self, to, p):
        self.tos.append(to)
        self.price.append(p)

class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:

        lines = []
        f = []
        inf = 1000011

        for i in range(n):
            lines.append(Flight())

            lst = []
            for j in range(k + 2):
                lst.append(inf)
            f.append(lst)


        
        for flight in flights:
            fr = flight[0]
            to = flight[1]
            price = flight[2]

            lines[fr].add_flight(to, price)

        for i in range(k + 2):
            f[src][i] = 0

        q_dest = [src]
        q_k = [0]

        ans = inf

        while(len(q_dest) != 0):
            fr = q_dest[0]
            stop = q_k[0]

            q_dest.remove(fr)
            q_k.remove(stop)

            for i in range(len(lines[fr].tos)):
                to = lines[fr].tos[i]
                price = lines[fr].price[i]

                if(f[to][stop + 1] > (f[fr][stop] + price)):
                    f[to][stop + 1] = f[fr][stop] + price
                    
                    if(to == dst):
                        ans = min(ans, f[to][stop + 1])
                    elif(stop < k):
                        q_dest.append(to)
                        q_k.append(stop + 1)

        if(ans == inf):
            ans = -1
            
        return ans