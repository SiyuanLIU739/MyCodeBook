class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height)
        right = [0] * len(height)

        for i in range(len(height)):
            left[i] = height[i]

            if(i > 0):
                left[i] = max(left[i], left[i - 1])
                
        for i in range(len(height) - 1, -1, -1):
            right[i] = height[i]

            if(i < (len(height) - 1)):
                right[i] = max(right[i], right[i + 1])

        ans = 0

        for i in range(len(height)):
            ans += (min(left[i], right[i]) - height[i])

        return ans

