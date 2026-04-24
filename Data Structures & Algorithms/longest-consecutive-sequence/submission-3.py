class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)
        max_count = 0
        for i in nums:
            if i-1 in vals:
                continue
            count = 1
            while i + count in vals:
                count += 1
            max_count = max(max_count, count)
        return max_count
            