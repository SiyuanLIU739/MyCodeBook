class Solution:
    def calculate2(self, s: str) -> int:
        if(s[0] != '('):
            s = "0" + s
        leftp = []
        sprime = ""
        for i in range(len(s)):
            if(s[i] == ')'):
                cal = self.basic_calculate(sprime[leftp[-1] + 1: ])
                sprime = sprime[: leftp[-1]]
                if(len(sprime) == 0):
                    sprime = str(cal)
                    continue
                j = -1
                while(sprime[j] == " "):
                    j -= 1

                if(cal < 0):
                    if(sprime[j] in '1234567890('):
                        sprime = sprime + str(cal)
                    elif(sprime[j] == '-'):
                        sprime = sprime[: len(sprime) + j] + '+' + str(-cal)
                    else:
                        sprime = sprime[: len(sprime) + j] + str(cal)
                else:
                    if(sprime[j] == '-'):
                        sprime = sprime[: len(sprime)] + str(cal)
                    else:
                        sprime = sprime[: len(sprime) + j] + "+" + str(cal)
                leftp.pop()

            else:
                sprime += s[i]
                if(s[i] == '('):
                    leftp.append(len(sprime) - 1)
        return self.basic_calculate(sprime)
    
    def basic_calculate(self, s):
        # split to values
        num = 0
        func = []

        # remove all blanks
        sprime = ""
        for char in s:
            if(char != ' '):
                sprime += char
        s = sprime

        for char in s:
            if(char in "1234567890"):
                num = num * 10 + int(char)
            else:
                func.append(num)
                func.append(char)
                num = 0
        func.append(num)

        ans = func[0]

        i = 1
        while(i < len(func)):
            if(func[i] == '+'):
                ans = ans + func[i + 1]
            else:
                ans = ans - func[i + 1]

            i += 2

        return ans
    
    def calculate(self, s: str) -> int:
        # filter out space
        sprime = ""
        for char in s:
            if(char != ' '):
                sprime += char
        if(sprime[0] == '-'):
            sprime = '0' + sprime
        s = sprime
        sprime = ""

        leftp = []

        for char in s:
            if(char == ')'):
                cal = self.basic_calculate(sprime[leftp[-1] + 1: ])
                sprime = sprime[: leftp[-1]]
                leftp.pop()

                if(len(sprime) == 0 or sprime[-1] == '('):
                    sprime = sprime + str(cal)
                elif(sprime[-1] == '+'):
                    if(cal < 0):
                        sprime = sprime[: -1] + str(cal)
                    else:
                        sprime = sprime + str(cal)
                elif(sprime[-1] == '-'):
                    if(cal < 0):
                        sprime = sprime[: -1] + '+' + str(-cal)
                    else:
                        sprime = sprime + str(cal)
            else:
                sprime += char
                if(char == '('):
                    leftp.append(len(sprime) - 1)

        return self.basic_calculate(sprime)

    
sol = Solution()
print(sol.calculate("((-(2 + 3)))"))

