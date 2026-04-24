class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        tracker_dict = {}

        for i in nums:
            tracker_dict[i] = tracker_dict.get(i, 0) + 1
        
        tracker_list = []
        for i in nums:
            tracker_list.append([])

        for i in tracker_dict:
            tracker_list[tracker_dict[i]-1].append(i)
        
        result = []
        for i in tracker_list[::-1]:
            result.extend(i)
        
        return result[:k]