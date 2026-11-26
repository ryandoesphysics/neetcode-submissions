class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            return [nums] if sum(nums) == 0 else []
                
        nums.sort()
        res = []

        for i in range(len(nums)):
            target = -nums[i]
            l, r = 0, len(nums)-1
            while l < r:
                if l == i:
                    l += 1
                    continue
                if r == i:
                    r -= 1
                    continue
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    if sorted([nums[i],nums[l],nums[r]]) not in res:
                        res.append(sorted([nums[i],nums[l],nums[r]]))
                    l += 1
        return res


                    