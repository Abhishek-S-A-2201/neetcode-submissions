class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ptr = 0
        start = ptr

        def twoSum(numbers: List[int], target: int):
            left = 0
            right = len(numbers)-1
            result = []

            while left < right:
                val = numbers[left]+numbers[right]
                if target == val:
                    result.append([numbers[left], numbers[right]])
                    left += 1
                    right -= 1
                elif val < target:
                    left += 1
                else:
                    right -= 1
            return result

        result = []
        for i in range(len(nums)-2):
            # if i > 0 and nums[i-1] == nums[i]:
            #     continue
            two_sum = twoSum(nums[i+1:], -nums[i])
            if two_sum:
                for s in two_sum:
                    s.append(nums[i])
                    result.append(tuple(sorted(s)))

        print(result)

        return list(set(result))
