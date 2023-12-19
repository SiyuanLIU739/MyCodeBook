import math

class Solution:
    f = []
    factorMap = []
    def numFactoredBinaryTrees(self, arr) -> int:
        self.f = [0] * len(arr)
        self.factorMap = []

        arr.sort()

        for i in range(len(arr)):
            self.factorMap.append([])

            for j in range(i):
                if(arr[i] % arr[j] > 0):
                    continue

                b = arr[i] / arr[j]
                if(b in arr):
                    self.factorMap[i].append(j)

        ans = 0
        for i in range(len(arr)):
            ans += self.findF(arr, i)
            ans %= (1000000007)

        return ans
    
    def findF(self, arr, i):
        if(self.f[i] != 0):
            return self.f[i]
        
        ans = 1

        if(len(self.factorMap[i]) != 0):
            x = arr[i]

            for a in self.factorMap[i]:
                bValue = x / arr[a]
                b = arr.index(bValue)

                ans += self.findF(arr, a) * self.findF(arr, b)

        self.f[i] = ans
        return ans



        

        



        




sol = Solution()
arr = [2,4, 5, 10]
print(sol.numFactoredBinaryTrees(arr))