class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if(s1 == s2):
            return True

        s1 = '1' + s1
        
        s3214 = s1[3] + s1[2] + s1[1] + s1[4]
        if(s3214 == s2):
            return True
        
        s1432 = s1[1] + s1[4] + s1[3] + s1[2]
        if(s1432 == s2):
            return True
        
        s3412 = s1[3] + s1[4] + s1[1] + s1[2]
        if(s3412 == s2):
            return True
        
        return False