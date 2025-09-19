class Solution:
    def decodeString(self, s: str) -> str:
        splited = []
        ans = ""

        for i in range(len(s)):
            if(i == 0):
                splited.append(s[i])
            else:
                # digit
                if(s[i] in "0123456789"):
                    if(s[i - 1] in "1234567890"):
                        splited[-1] = splited[-1] + s[i]
                    else:
                        splited.append(s[i])
                elif(s[i] == "["):
                    splited.append(s[i])
                elif(s[i] in "qwertyuiopasdfghjklzxcvbnm"):
                    if(s[i - 1] in "qwertyuiopasdfghjklzxcvbnm"):
                        splited[-1] = splited[-1] + s[i]
                    else:
                        splited.append(s[i])
                elif(s[i] == ']'):
                    # must be str
                    substr = splited.pop()
                    # must be left bracket
                    leftbracket = splited.pop()
                    while(leftbracket != "["):
                        substr = leftbracket + substr
                        leftbracket = splited.pop()
                    # might be times
                    times = 1
                    try:
                        times = int(splited.pop())
                    except:
                        times = 1
                    result = times * substr
                    # might be a str or a left bracket
                    last = ""
                    if(len(splited) > 0 and splited[-1] != '['):
                        last = splited.pop()
                    result = last + result
                    
                    splited.append(result)

        for s in splited:
            ans += s

        return ans