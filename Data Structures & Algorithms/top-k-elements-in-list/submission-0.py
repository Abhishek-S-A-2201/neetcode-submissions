class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mapping = {}
        for i in nums:
            if i in mapping:
                mapping[i] += 1
            else:
                mapping[i] = 1
        
        freq = [[] for i in range(len(nums))]
        for i in mapping:
            freq[mapping[i]-1].append(i)
        res = []
        for j in freq[::-1]:
            for l in j:
                if len(res) == k:
                    return res
                res.append(l)

        return res