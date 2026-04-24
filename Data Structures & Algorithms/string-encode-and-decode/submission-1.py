class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}${s}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        l = 0
        while l < len(s):
            digit = ''
            while not s[l] == "$":
                digit += s[l]
                l += 1
            digit = int(digit)
            res.append(s[l+1:l+1+digit])
            l = l+1+digit
        
        return res