import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        pq = [1]
        for i in range(1, n):
            num = heapq.heappop(pq)
            max_prime = 1
            for prime in primes:
                if(num % prime == 0):
                    max_prime = prime
            for prime in primes:
                if(prime < max_prime):
                    continue
                heapq.heappush(pq, num * prime)

        return heapq.heappop(pq)