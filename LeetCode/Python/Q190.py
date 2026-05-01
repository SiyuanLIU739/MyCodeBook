class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""

        while(n != 0):
            binary += str(n % 2)
            n = n >> 1

        binary = binary + "0" * (32 - len(binary))

        ans = 0
        for digit in binary:
            ans *= 2
            if(digit == '1'):
                ans += 1

        return ans