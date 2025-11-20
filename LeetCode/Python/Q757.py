class Interval:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.count = 0

    def __lt__(self, other):
        if(self.r != other.r):
            return self.r < other.r
        return self.l > other.l
    

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals_struc = []

        for i in intervals:
            intervals_struc.append(Interval(i[0], i[1]))

        intervals_struc.sort()

        ans = []
        for i in intervals_struc:
            if(i.count >= 2):
                continue

            j = i.r
            while(i.count < 2 and j >= i.l):
                if(j not in ans):
                    ans.append(j)
                    for interval in intervals_struc:
                        if(interval.l <= j and interval.r >= j):
                            interval.count += 1
                j -= 1
        return len(ans)
                