class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        tracker = {}

        for i in range(len(nums)):
            if nums[i] in tracker:
                return [tracker[nums[i]], i]
            else:
                tracker[target - nums[i]] = i