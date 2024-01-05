class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        devices = []

        for i in range(len(bank)):
            cnt = 0

            for j in range(bank[i]):
                if(j == '1'):
                    cnt += 1
            
            devices.append(cnt)

        ans = 0
        for i in range(1, len(bank)):
            ans += devices[i - 1] * devices[i]
        return ans