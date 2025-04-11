class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0

        if(not (low >= 100 or high <= 10)):
            ans += self.findTwoDigits(low, high)

        if(not (low >= 10000 or high <= 1000)):
            ans += self.findFourDigits(max(low, 1000), min(high, 10000))

        return ans

    def findTwoDigits(self, low, high):
        ret = 0

        for i in range(1, 10):
            num = i * 11
            if(num >= low and num <= high):
                ret += 1

        return ret
    
    def findFourDigits(self, low, high):
        ret = 0

        for i in range(low, high + 1):
            if(((i // 1000) + ((i // 100) % 10)) == ((i // 10) % 10) + (i % 10)):
                ret += 1
        
        return ret