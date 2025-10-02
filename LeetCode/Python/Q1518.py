class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        ans = numBottles

        while (numBottles >= numExchange):
            water = numBottles // numExchange
            extrabottle = numBottles % numExchange

            ans += water
            numBottles = water + extrabottle

        return ans