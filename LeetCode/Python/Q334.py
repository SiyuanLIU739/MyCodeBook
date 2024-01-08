class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = [2147483647]

        for num in nums:
            if(num > a[-1]):
                a.append(num)
            else:
                for i in range(len(a)):
                    if(num <= a[i]):
                        a[i] = num
                        break
            
            if(len(a) == 3):
                return True
                
        return False