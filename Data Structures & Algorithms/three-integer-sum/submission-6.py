class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            return [nums] if sum(nums) == 0 else []
                
        nums.sort()
        res = []

        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    if sorted([nums[i],nums[l],nums[r]]) not in res:
                        res.append(sorted([nums[i],nums[l],nums[r]]))
                    l += 1
                    r -= 1
                    # while left<right and nums[left]==nums[left-1]:
                    #     left += 1
        return res


                    