class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for num in nums:
            hash[num] = hash.get(num, 0) + 1
        frequencies = (sorted(hash.items(), key = lambda item: item[1], reverse = True))
        return [pair[0] for pair in frequencies[0:k]]