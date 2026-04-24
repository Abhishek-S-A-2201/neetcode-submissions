class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)
        max_count = 0
        for i in nums:
            count = 1
            if i-1 in vals:
                continue
            temp = i+1
            while temp in vals:
                count += 1
                temp += 1
            max_count = max(max_count, count)
        return max_count
            