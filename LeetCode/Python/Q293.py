class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        n = len(currentState)

        ans = []
        for i in range(1, n):
            if(currentState[i - 1: i + 1] == '++'):
                ans.append(currentState[: i - 1] + '--' + currentState[i + 1: ])

        return ans