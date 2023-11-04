class Solution:
    def buildArray(self, target, n: int):
        ans = []
        target.insert(0, 0)
        j = 1

        for i in range(1, n + 1):
            if(i == target[j]):
                for k in range(target[j] - target[j - 1] - 1):
                    ans.append('pop')

                j += 1
            
            ans.append('push')

            if(j >= len(target)):
                break
            
        return ans

sol = Solution()
print(sol.buildArray([1, 2, 3], 4))