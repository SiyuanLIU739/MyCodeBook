class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.append([0, 11])
        reservedSeats.append([n + 1, 1])
        reservedSeats.sort()
        n = len(reservedSeats)

        ans = 0
        i = 0
        currentRow = 0
        while(i < n - 1):
            i += 1
            l = reservedSeats[i - 1][1]
            r = reservedSeats[i][1]

            if(reservedSeats[i][0] != currentRow):
                ans += 2 * (reservedSeats[i][0] - currentRow - 1)

                currentRow = reservedSeats[i][0]

                if(l < 2):
                    ans += 2
                elif(l < 6):
                    ans += 1
                
                if(r > 9):
                    ans += 2
                elif(r > 5):
                    ans += 1
                
                continue

                
            
            if(l < 2 and r > 9):
                ans += 2
            elif(l < 2 and r > 5):
                ans += 1
            elif(l < 4 and r > 7):
                ans += 1
            elif(l < 6 and r > 9):
                ans += 1

        return ans