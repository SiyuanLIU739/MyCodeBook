class Interval:
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __lt__(self, other):
        return self.r < other.r

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        times = []
        for interval in intervals:
            times.append(Interval(interval[0], interval[1]))

        times = sorted(times)

        count = 1
        last = times[0].r

        for i in range(1, len(times)):
            time = times[i]
            if(time.l >= last):
                count += 1
                last = time.r

        return len(intervals) - count