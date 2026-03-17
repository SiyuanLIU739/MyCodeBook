class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [0] * len(ratings)

        if(n == 1):
            return 1
        
        if(ratings[0] <= ratings[1]):
            candies[0] = 1

        for i in range(1, n):
            j = -1
            if(i == (n - 1)):
                if(ratings[i - 1] >= ratings[i]):
                    candies[i] = 1
                    j = i - 1
                else:
                    candies[i] = candies[i - 1] + 1
            else:
                if(ratings[i] > ratings[i + 1]):
                    continue
                else:
                    if(ratings[i - 1] < ratings[i]):
                        candies[i] = candies[i - 1] + 1
                    else:
                        candies[i] = 1
                        j = i - 1

            while(j != -1 and candies[j] == 0):
                if(j == 0 or ratings[j - 1] == ratings[j]):
                    candies[j] = candies[j + 1] + 1
                else:
                    candies[j] = max(candies[j - 1], candies[j + 1]) + 1
                j -= 1

        ans = 0
        for i in range(n):
            ans += candies[i]
        return ans