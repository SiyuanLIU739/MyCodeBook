class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = {}

        for num in arr:
            if(num not in freq.keys()):
                freq[num] = 0

            freq[num] += 1

        f = []
        for key, value in freq.items():
            f.append(value)

        n = len(f)
        f.sort()
        cnt = 0

        for num in f:
            if(k >= num):
                cnt += 1
                k -= num
            else:
                break
        
        return n - cnt