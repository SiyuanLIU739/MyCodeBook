class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        arr.insert(0, 0)

        f = [0] * len(arr)

        for i in range(1, len(arr)):
            maxArr = arr[i]
            for j in range(1, k + 1):
                if(i - j < 0):
                    break
                f[i] = max(f[i], f[i - j] + maxArr * j)
                maxArr = max(maxArr, arr[i - j])

        return f[-1]