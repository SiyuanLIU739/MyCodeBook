class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:

        d1 = max(arriveAlice, arriveBob)
        d2 = min(leaveAlice, leaveBob)

        from datetime import datetime

        d1 = datetime.strptime(d1, "%m-%d")
        d2 = datetime.strptime(d2, "%m-%d")

        days = (d2 - d1).days + 1

        if(days < 0):
            return 0
        return days