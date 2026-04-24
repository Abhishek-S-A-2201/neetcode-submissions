class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result += f"{len(i)}${i}"
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []

        ptr = 0
        start = ptr
        while ptr < len(s):
            if s[ptr+1] != "$":
                ptr += 1
                continue
            else:
                num = int(s[start: ptr+1])
                print(num)
                if num == 0:
                    result.append("")
                else:
                    result.append(s[ptr+2: ptr+num+2])
                ptr += num + 2
                print(ptr)
                start = ptr
        
        return result