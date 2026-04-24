class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0
        while i < len(nums):
            l = i+1
            r = len(nums)-1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val < 0:
                    l += 1
                elif val > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
            i += 1
            while i < len(nums) and nums[i-1] == nums[i]:
                i += 1
        return res
