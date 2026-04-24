class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        max_len = 0
        for i in nums:
            if i-1 not in unique:
                count = 1
                while i+1 in unique:
                    count += 1
                    i += 1
                max_len = max(count, max_len)
        return max_len
