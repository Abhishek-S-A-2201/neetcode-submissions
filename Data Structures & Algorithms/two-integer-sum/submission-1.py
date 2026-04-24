class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        
        indexes = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indexes:
                return [indexes[diff], i]
            else:
                indexes[nums[i]] = i 
        