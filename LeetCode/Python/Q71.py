class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")

        ret = []

        for folder in path:
            if(folder == '' or folder == "."):
                continue
            if(folder == ".."):
                if(len(ret) > 0):
                    ret.pop()
            else:
                ret.append(folder)

        ret = "/".join(ret)

        ret = "/" + ret
        return ret