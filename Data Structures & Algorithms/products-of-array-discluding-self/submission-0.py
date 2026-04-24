class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre, post = [1], [1]
        for i in range(len(nums)):
            pre.append(pre[i]*nums[i])
            post.append(post[i]*nums[len(nums)-i-1])
        post = post[::-1]
        res = []
        for i in range(len(pre)-1):
            res.append(pre[i]*post[i+1])
        
        return res