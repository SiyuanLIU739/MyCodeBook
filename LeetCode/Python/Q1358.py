class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        s = " " + s
        fa = [0]
        fb = [0]
        fc = [0]

        for i in range(1, len(s)):
            fa.append(fa[-1])
            fb.append(fb[-1])
            fc.append(fc[-1])

            if(s[i] == 'a'):
                fa[-1] += 1
            if(s[i] == 'b'):
                fb[-1] += 1
            if(s[i] == 'c'):
                fc[-1] += 1

        ans = 0
        for i in range(1, len(s)):
            if(fa[i] == 0 or fb[i] == 0 or fc[i] == 0):
                continue
            
            index = len(s) * 2
            index = min(index, self.find_index(fa, 0, i, fa[i] - 1))
            index = min(index, self.find_index(fb, 0, i, fb[i] - 1))
            index = min(index, self.find_index(fc, 0, i, fc[i] - 1))

            if(index == -1):
                continue

            ans += index
        
        return ans

    def find_index(self, f, l, r, target):
        result = -1
        while(l <= r):
            mid = (l + r) // 2
            if(f[mid] == target):
                result = mid

            if(f[mid] <= target):
                l = mid + 1
            else:
                r = mid - 1

        return result