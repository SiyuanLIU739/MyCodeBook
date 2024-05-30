class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = 0

        for i in range(len(matrix)):
            ones = [True] * len(matrix[0])

            for j in range(i, len(matrix)):
                length = [0]
                width = 0
                
                for k in range(len(matrix[0])):
                    ones[k] = (ones[k] and (matrix[j][k] == '1'))
                    if(ones[k] == True):
                        length.append(length[-1] + 1)
                        width = max(width, length[-1])

                    else:
                        length.append(0)

                ans = max(ans, (j - i + 1) * width)

        return ans