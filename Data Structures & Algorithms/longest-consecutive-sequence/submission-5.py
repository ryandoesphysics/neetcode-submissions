class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # inverse hashmap since we dont care about the index
        # max = 0
        # for loop go through nums
        # if for any n in nums, n-1 is not in values, that is the start of a sequence
        #   select that start, check if n+1 is in nums, if yes keep checking and keep count
        #   if not then end and move on to the next n
        # else: n-1 is in values, next n
        hm = {v:i for i,v in enumerate(nums)}
        consec = 0
        for n in hm.keys():
            if (n - 1) not in hm.keys():
                # this is the start of the sequence
                m = 1
                while n + m in hm.keys():
                    m += 1
                consec = max(m,consec)
        return consec