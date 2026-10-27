class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        out = []
        for i in range(m):
            string = ""
            for j in range(n):
                if i == 0:
                    string = "".join([string, "."])
                elif j == n-1:
                    string = "".join([string, "."])
                else:
                    string = "".join([string, "#"])

            out.append(string)
        return out