class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         
        groups = {}

        for i in strs:
            chars = [0]*26
            for s in i:
                chars[ord(s)-ord('a')] += 1
            chars = tuple(chars)
            if chars in groups:
                groups[chars].append(i)
            else:
                groups[chars] = [i]

        return groups.values() 
        