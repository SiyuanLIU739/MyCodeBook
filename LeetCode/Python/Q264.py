class Solution:
    def nthUglyNumber(self, n: int) -> int:
        found = [1]
        multipliers = [2, 3, 4, 5]
        i = 0

        while(len(found) < n * 2):
            num = found[i]
            i += 1
            for multiplier in multipliers:
                if(num * multiplier not in found):
                    found.append(num * multiplier)
        found.sort()
        return found[n - 1]
    
sol = Solution()
for i in range(1, 16):
    print(sol.nthUglyNumber(i))