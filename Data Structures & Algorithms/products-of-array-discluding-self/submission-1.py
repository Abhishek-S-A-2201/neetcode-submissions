class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        pre = 1
        for i in nums:
            pre *= i
            prefix.append(pre)
        
        postfix = [1]
        post = 1
        for i in nums[::-1]:
            post *= i
            postfix.append(post)

        prefix = prefix[:-1]
        postfix = postfix[:-1][::-1]

        result = []
        for i in range(len(prefix)):
            result.append(postfix[i]*prefix[i])
        
        return result