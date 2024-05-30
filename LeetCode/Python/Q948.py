class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        s = sum(tokens)

        if(s <= power):
            return n
        
        tokens.sort(reverse = True)

        score = 0
        l = 0
        r = n - 1

        while(l <= r):
            while(l <= r and tokens[r] <= power):
                power -= tokens[r]
                r -= 1
                score += 1
            
            if(l < r and score > 0):
                power += tokens[l]
                l += 1
                score -= 1

            else:
                break

        l -= 1
        while(l >= 0 and power >= tokens[l]):
            power -= tokens[l]
            l -= 1
            score += 1

        return score