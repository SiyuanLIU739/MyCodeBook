class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        sum = [0] * (n + 1)

        for booking in bookings:
            sum[booking[0] - 1] += booking[2]
            sum[booking[1]] -= booking[2]
        
        ans = []
        tot = 0
        for s in sum:
            tot += s
            ans.append(tot)

        return ans[: -1]
        