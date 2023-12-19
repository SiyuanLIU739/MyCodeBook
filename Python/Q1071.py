class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if(len(str1) < len(str2)):
            str3 = str1
            str1 = str2
            str2 = str3

        return self.count(str1, str2)
    
    def count(self, str1, str2):
        if(str2 == ""):
            return str1
        
        for i in range(len(str2)):
            if(str1[i] != str2[i]):
                return ""
            
        if(len(str1) > 2 * len(str2)):
            return self.count(str1[len(str2): ], str2)
        return self.count(str2, str1[len(str2): ])
    