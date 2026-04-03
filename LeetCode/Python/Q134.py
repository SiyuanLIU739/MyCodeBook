class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        gasLeft = 0
        start = n - 1
        arrived = n - 1
        stationVisited = 0

        while(stationVisited < n):
            if(gasLeft < 0):
                start -= 1
                gasLeft = gasLeft + gas[start] - cost[start]
            else:
                gasLeft = gasLeft + gas[arrived] - cost[arrived]
                arrived = (arrived + 1) % n
            stationVisited += 1

        if(gasLeft < 0):
            return -1
        return start