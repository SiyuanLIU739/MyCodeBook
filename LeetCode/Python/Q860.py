class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        existing = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            if(bill == 5):
                existing[5] += 1
            elif(bill == 10):
                if(existing[5] > 0):
                    existing[5] -= 1
                    existing[10] += 1
                else:
                    return False
            else:
                if(existing[10] >= 1 and existing[5] >= 1):
                    existing[5] -= 1
                    existing[10] -= 1
                    existing[20] += 1
                elif(existing[5] >= 3):
                    existing[5] -= 3
                    existing[20] += 1
                else:
                    return False
            
        return True