class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest_str = min(strs)
        common = ""
        for i in range(len(smallest_str)):
            flag = True
            for j in strs:
                if j[i] != smallest_str[i]:
                    flag = False
                    break                    

            if not flag:
                break
            else:
                common += smallest_str[i]
                
        return common
        