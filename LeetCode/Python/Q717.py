class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if(len(bits) == 1):
            return True
        
        if(bits[-1] == 1):
            return False

        nextErased = False
        for i in range(len(bits) - 1):
            if(nextErased):
                nextErased = False
                continue
            if(bits[i] == 1):
                nextErased = True

        if(nextErased):
            return False
        return True