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

# nums = [1,2,4,6]
# pre = [1,2,8,48]
# post = [48,48,24,6]

# nums = [1,2,3,4,5]
# pre = [1,2,6,24,120]
# post = [120,120,60,20,5]


            