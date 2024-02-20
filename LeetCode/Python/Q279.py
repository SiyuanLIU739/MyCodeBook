class Solution:
    def numSquares(self, n: int) -> int:
        numbers = []
        for i in range(1, n):
            numbers.append(i ** 2)
            if(numbers[-1] >= n):
                break

        f = [n] * (n + 1)
        f[0] = 0
        
        queue = [0]

        while(queue.__len__() != 0):
            current = queue.pop(0)

            for num in numbers:
                if(num + current > n):
                    continue
                
                if(f[num + current] > f[current] + 1):
                    f[num + current] = f[current] + 1

                    if(num + current == n):
                        return f[num + current]
                    
                    queue.append(num + current)

        return -1