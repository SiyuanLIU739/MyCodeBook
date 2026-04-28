class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        return self.constructArray(n)
    
    def constructArray(self, n):
        if(n == 1):
            return [1]
        
        left = n // 2
        right = n // 2
        if(n % 2 == 1):
            left += 1

        left = self.constructArray(left)
        right = self.constructArray(right)

        ans = []
        for num in left:
            ans.append(num * 2 - 1)
        for num in right:
            ans.append(num * 2)

        return ans