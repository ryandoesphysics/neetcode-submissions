class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # if non decreasing array, -> the list can have increasing or same number
        l, r = 0, len(numbers)-1
        hm = {i:v for i,v in enumerate(numbers)}
        while l < r:
            if hm[l] + hm[r] > target:
                r -= 1
            elif hm[l] + hm[r] < target:
                l += 1
            else:
                return [l+1, r+1]
        