class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        books.insert(0, [0, 0])

        f = [1000 * 1000 * 2] * len(books)
        f[0] = 0

        for i in range(1, len(books)):
            width = 0
            maxheight = 0
            for j in range(1, len(books)):
                lst = i - j
                if(lst < 0):
                    break

                maxheight = max(maxheight, books[lst + 1][1])
                width += books[lst + 1][0]
                if(width > shelfWidth):
                    break

                f[i] = min(f[i], f[lst] + maxheight)
            
        return f[-1]