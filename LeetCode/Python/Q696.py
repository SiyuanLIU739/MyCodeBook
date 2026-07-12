class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        left = -1
        count_left = 0

        ans = 0
        n = len(s)
        while(left < n - 1):
            left += 1
            count_left += 1
            if(left == n - 1 or s[left] != s[left + 1]):
                break

        if(left == n - 1):
            return ans
        
        right = left + 1
        count_right = 1
        while(left < n - 1):
            while(right < n - 1 and s[right] == s[right + 1]):
                right += 1
                count_right += 1
            
            ans += min(count_left, count_right)
            left = right
            count_left = count_right
            right = left + 1
            count_right = 1

        return ans