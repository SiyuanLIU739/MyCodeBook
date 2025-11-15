class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        numept = numBottles

        while(numept >= numExchange):
            ans = ans + 1
            numept = numept - numExchange + 1
            numExchange += 1

        return ans
