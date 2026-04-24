class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        tracker_dict = {}
        
        for i in strs:
            tracker = [0]*26
            for j in i:
                tracker[ord(j)-ord('a')] += 1
            if tuple(tracker) in tracker_dict:
                tracker_dict[tuple(tracker)].append(i)
            else:
                tracker_dict[tuple(tracker)] = [i]
        
        return list(tracker_dict.values())
        
        