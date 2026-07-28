class Solution:

    def encode(self, strs: List[str]) -> str:
        # for i in range(len(strs) - 1):
        #     s += f"{strs[i]}:."
        # s += f"{strs[len(strs) - 1]}:"
        if len(strs) == 0:
            return ""
        s = ":.".join(strs) + ":"
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        strs = []
        for elem in s.rsplit("."):
            strs.append(elem[:-1])
        return strs