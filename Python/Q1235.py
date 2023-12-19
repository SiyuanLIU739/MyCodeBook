class Job:
    def __init__(self, s, t, p):
        self.s = s
        self.t = t
        self.p = p

    def __lt__(self, other):
        return self.t < other.t
    


class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        jobs = []
        for i in range(len(profit)):
            jobs.append(Job(startTime[i], endTime[i], profit[i]))

        jobs.sort()

        f = []
        fmax = []

        for i in range(len(jobs)):
            index = self.binarySearch(jobs, 0, i - 1, jobs[i].s)

            if(index == -1):
                f.append(jobs[i].p)
                fmax.append(max(f[i], fmax[i - 1] if i > 0 else 0))

            else:
                f.append(jobs[i].p + fmax[index])
                fmax.append(max(f[i], fmax[i - 1]))

        return fmax[-1]
    
    def binarySearch(self, jobs, s, t, target):
        if(jobs[0].t > target):
            return -1
        
        if(s == t):
            return s
        
        mid = (int)((s + t) / 2)

        if(jobs[mid + 1].t == target):
            return self.binarySearch(jobs, mid + 1, t, target)
        
        if(jobs[mid].t > target):
            return self.binarySearch(jobs, s, mid, target)
        if(jobs[mid + 1].t < target):
            return self.binarySearch(jobs, mid + 1, t, target)
        return mid
        

        

sol = Solution()
startTime = [6,15,7,11,1,3,16,2]
endTime = [19,18,19,16,10,8,19,8]
profit = [2,9,1,19,5,7,3,19]
print(sol.jobScheduling(startTime, endTime, profit))