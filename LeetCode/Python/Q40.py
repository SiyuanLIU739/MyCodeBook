class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.counts = {}

        for i in range(len(candidates)):
            if(candidates[i] not in self.counts.keys()):
                self.counts[candidates[i]] = 0
            self.counts[candidates[i]] += 1

        self.nums = list(self.counts.keys())

        self.ans = []
        self.comb([], 0, 0, target)

        return self.ans
    
    def comb(self, lst, i, s, target):
        if(i == len(self.nums)):
            if(s == target):
                self.ans.append(lst.copy())

            return
        
        for j in range(self.counts[self.nums[i]] + 1):
            if(s + j * self.nums[i] > target):
                break

            self.comb(lst + [self.nums[i]] * j, i + 1, s + j * self.nums[i], target)

        return