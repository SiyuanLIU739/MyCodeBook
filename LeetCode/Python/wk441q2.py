class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        index = {}

        for i in range(len(nums)):
            num = nums[i]

            if(num not in index.keys()):
                index[num] = []

            index[num].append(i)

        ans = []

        for q in queries:
            num = nums[q]
            
            ind = index[num]

            if(len(ind) == 1):
                ans.append(-1)
            else:
                l = 0
                r = len(ind) - 1

                while(l < r):
                    mid = (l + r) // 2
                    if(ind[mid] == q):
                        l = mid
                        r = mid
                        break

                    if(ind[mid] < q):
                        l = mid + 1
                    else:
                        r = mid - 1

                lind = 0
                rind = 0
                if(l == 0):
                    lind = ind[-1]
                    rind = ind[1]
                elif(r == len(ind) - 1):
                    lind = ind[0]
                    rind = ind[r - 1]
                else:
                    lind = ind[l - 1]
                    rind = ind[r + 1]

                a = abs(lind - q)
                d1 = min(a, len(nums) - a)
                a = abs(rind - q)
                d2 = min(a, len(nums) - a)

                ans.append(min(d1, d2))
        return ans