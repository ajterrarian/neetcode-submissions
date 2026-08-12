class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            initial = nums[i]
            if initial in hashmap:
                return True

            else:
                hashmap[nums[i]] = i
        
        return False