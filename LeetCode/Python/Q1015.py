class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        reminders = []

        len = 0
        num = 0
        while(True):
            len += 1
            num = (num * 10 + 1) % k

            if(num == 0):
                return len

            if(num in reminders):
                return -1

            reminders.append(num)

        return -1
