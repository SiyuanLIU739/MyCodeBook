from bisect import bisect_right

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        h = []
        starts = []

        for i in range(len(nums)):
            if(i == 0 or nums[i - 1] > nums[i]):
                starts.append(i)
                h.append(i)
            else:
                h.append(h[-1])

        ans = 0
        for i in range(len(nums)):
            k = i + 1
            if(len(nums) % k != 0):
                continue

            vio = False

            st = 0
            ed = st + k - 1
            last_max = 0

            while(ed < len(nums)):

                if(h[st] == h[ed]):
                    if(last_max <= nums[st]):
                        last_max = nums[ed]
                        st = ed + 1
                        ed = st + k - 1
                        continue
                    else:
                        vio = True
                        break

                loc_first = bisect_right(starts, st)
                loc_last = bisect_right(starts, ed) - 1
                count = loc_last - loc_first + 1

                if(count > 1):
                    vio = True
                    break

                if(nums[st] < nums[ed]):
                    vio = True
                    break
          
                this_max = nums[starts[loc_last] - 1]

                if(nums[starts[loc_last]] < last_max):
                    vio = True
                    break
        
                last_max = this_max
                st = ed + 1
                ed = st + k - 1
                continue

            if(not vio):
                ans += k

        return ans