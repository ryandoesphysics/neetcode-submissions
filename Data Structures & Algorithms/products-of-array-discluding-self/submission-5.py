class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        postfix = [0]*n
        for i in range(n):
            if i == 0:
                prefix[0] = nums[0]
                postfix[-1] = nums[-1]
            else:
                prefix[i] = nums[i]*prefix[i-1]
                postfix[n - 1 - i] = nums[n - 1 -i]*postfix[n-i]
        
        res = []
        for i in range(n):
            if i == 0:
                res.append(postfix[1])
            elif i == n - 1:
                res.append(prefix[-2])
            else:
                res.append(postfix[i+1]*prefix[i-1])
        return res


            