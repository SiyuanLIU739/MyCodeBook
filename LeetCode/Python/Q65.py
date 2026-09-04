class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()

        nums = s.split('e')

        if(len(nums) > 2):
            return False

        if(len(nums) == 2):
            exp = nums[1]

            if(len(exp) == 0):
                return False

            if(exp[0] in '+-'):
                exp = exp[1: ]

            elif(exp[0] not in '1234567890'):
                return False
            
            if(not self.isNoSignInteger(exp)):
                return False

        num = nums[0]
        if(len(num) == 0):
            return False
        
        if(num[0] in '+-'):
            num = num[1: ]
        elif(num[0] not in '1234567890.'):
            return False

        nums = num.split('.')
        if(len(nums) > 2):
            return False

        if(len(nums) == 2):
            if(len(nums[0]) == 0 and len(nums[1]) == 0):
                return False
            return (self.isNoSignInteger(nums[0]) or len(nums[0]) == 0) and (self.isNoSignInteger(nums[1]) or len(nums[1]) == 0)

        return self.isNoSignInteger(nums[0])
        


    def isNoSignInteger(self, s):
        if(len(s) == 0):
            return False
        
        for char in s:
            if(char not in '1234567890'):
                return False

        return True
        

