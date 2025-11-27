class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []

        n = len(nums1)
        pairs = []
        for i in range(n):
            pairs.append([i, 0])

        for i in range(k):
            ans.append(self.take_first(nums1, nums2, pairs))

        return ans
    
    def take_first(self, nums1, nums2, pairs):
        # take out the pair
        pair = pairs.pop(0)
        ret = [nums1[pair[0]], nums2[pair[1]]]

        # add another pair if necessary
        pair[1] += 1
        if(pair[1] < len(nums2)):
            l = 0
            r = len(pairs) - 1

            while(l <= r):
                mid = (l + r) // 2
                midpair = pairs[mid]
                if(nums1[pair[0]] + nums2[pair[1]] == nums1[midpair[0]] + nums2[midpair[1]]):
                    l = mid
                    break

                if(nums1[pair[0]] + nums2[pair[1]] < nums1[midpair[0]] + nums2[midpair[1]]):
                    r = mid - 1
                else:
                    l = mid + 1
            pairs.insert(l, pair)

        return ret