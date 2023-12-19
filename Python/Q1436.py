class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        fr = []
        to = []

        for path in paths:
            fr.append(path[0])
            to.append(path[1])

        for t in to:
            if(t not in fr):
                return t