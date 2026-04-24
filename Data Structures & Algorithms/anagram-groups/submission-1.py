from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            chars = [0]*26
            for k in s:
                chars[ord(k) - ord('a')] += 1
            hashmap[tuple(chars)].append(s)
        return list(hashmap.values())
        