class Solution:
    def minOperations(self, s: str) -> int:
        if(len(s) == 1):
            return 0
        
        if(len(s) == 2):
            if(ord(s[0]) <= ord(s[1])):
                return 0
            return -1

        ords = []
        for char in s:
            ords.append(ord(char))

        sorted_verify = True
        for i in range(1, len(ords)):
            if(ords[i] < ords[i - 1]):
                sorted_verify = False
                break

        if(sorted_verify):
            return 0

        smallest = ord('z') + 1
        largest = ord('a') - 1

        for o in ords:
            if(o < smallest):
                smallest = o
            if(o > largest):
                largest = o


        if(largest == ords[0] and smallest == ords[-1]):
            largest_count = 0
            smallest_count = 0
            for o in ords:
                if(o == largest):
                    largest_count += 1
                if(o == smallest):
                    smallest_count += 1
            if(largest_count + smallest_count != 2):
                return 2
            return 3

        if(largest == ords[-1] or smallest == ords[0]):
            return 1

        return 2