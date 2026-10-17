class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(list)
        c = Counter(nums)
        for x in c.keys():
            d[c.get(x)].append(x)
        sorted_freqs = sorted(d.keys(), reverse = True)
        n = []
        for freq in sorted_freqs:
            n += d[freq]
            if len(n) >= k:
                break
        return n[:k]