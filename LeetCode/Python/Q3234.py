class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        last0 = [-1] * n
        loc = -1
        for i in range(n):
            last0[i] = loc

            if(s[i] == '0'):
                loc = i
                
        ans = 0
        first1 = 0
        for j in range(n):
            if(s[j] == '0'):
                first1 = j + 1
            else:
                ans += (j - first1 + 1)
                
        for j in range(n):
            num0 = 1
            if(s[j] == '0'):
                left0 = j
            else:
                left0 = last0[j]

            while(left0 != -1 and num0 * num0 <= j):
                i = j - num0 - num0 * num0 + 1
                if(i < 0):
                    break
                if(left0 < i):
                    i = left0

                num0 += 1
                left0 = last0[left0]
                if(i < left0):
                    continue
                ans += (i - left0)

        return ans