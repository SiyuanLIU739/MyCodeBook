class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if(num not in freq.keys()):
                freq[num] = 0
            freq[num] += 1

        freq_list = []
        for key, value in freq.items():
            freq_list.append((key, value))

        freq_list.sort(key = lambda x: -x[1])

        ans = []
        for i in range(k):
            ans.append(freq_list[i][0])

        return ans