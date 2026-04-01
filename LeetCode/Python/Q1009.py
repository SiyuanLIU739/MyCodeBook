class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if(n == 0):
            return 1

        binaries = []

        while(n > 0):
            if (n % 2 == 0):
                binaries.append(1)
            else:
                binaries.append(0)

            n = n // 2

        ans = 0
        for i in range(len(binaries)):
            b = binaries[len(binaries) - i - 1]
            ans = ans * 2 + b

        return ans